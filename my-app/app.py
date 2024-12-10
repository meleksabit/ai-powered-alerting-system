import logging
from prometheus_client import start_http_server, Counter, generate_latest
from flask import Flask, Response, jsonify, request
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import os
import yagmail

# Add Mock for Slack (in case of testing)
try:
    from slack_bolt import App as SlackApp
    from slack_bolt.adapter.flask import SlackRequestHandler
    from unittest.mock import MagicMock
except ImportError:
    SlackApp = None
    SlackRequestHandler = None
    MagicMock = None

# Enable logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Check if the app is running in test mode
IS_TESTING = os.getenv("FLASK_ENV") == "testing"

# Slack app initialization
if IS_TESTING:
    SLACK_BOT_TOKEN = "mock-token"
    SLACK_SIGNING_SECRET = "mock-signing-secret"

    # Mock SlackApp and SlackRequestHandler during tests
    slack_app = MagicMock()
    slack_handler = MagicMock()
else:
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
    if not SLACK_BOT_TOKEN or not SLACK_SIGNING_SECRET:
        raise EnvironmentError("Slack credentials are missing. Please set them as environment variables.")

    slack_app = SlackApp(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)
    slack_handler = SlackRequestHandler(slack_app)

# Initialize Flask app
app = Flask(__name__)

# Define Prometheus Counters
log_severity = Counter('log_severity', 'Count of log severities', ['severity'])
email_sending_status = Counter('email_sending_status', 'Status of email sending', ['status'])

# Load email credentials from environment variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

if not SENDER_EMAIL or not RECIPIENT_EMAIL:
    raise EnvironmentError("Email credentials are missing. Please set them as environment variables.")

# Variables to hold the model and tokenizer, initialized as None
model = None
tokenizer = None
classifier = None

def lazy_load_model():
    """Lazy load the model and tokenizer for text classification."""
    global model, tokenizer, classifier
    if model is None or tokenizer is None or classifier is None:
        logging.info("Loading model and tokenizer lazily...")
        tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
        logging.info("Model and tokenizer loaded.")

def classify_log_event(log_message):
    """Classify log messages using Hugging Face DistilBERT model."""
    lazy_load_model()
    result = classifier(log_message)
    severity = 'not_critical' if result[0]['label'] == 'POSITIVE' else 'critical'
    log_severity.labels(severity=severity).inc()
    logging.info(f"Classified log '{log_message}' as {severity}")
    return severity

@app.route('/send_email/<log_message>')
def send_email_endpoint(log_message):
    """Send an email with the classified log message."""
    try:
        severity = classify_log_event(log_message)
        yag = yagmail.SMTP(SENDER_EMAIL)
        subject = "Log Alert: New Event Notification"
        body = f"Log Message: {log_message}\nSeverity: {severity}"
        yag.send(to=RECIPIENT_EMAIL, subject=subject, contents=body)
        email_sending_status.labels(status="success").inc()
        logging.info(f"Email sent successfully from {SENDER_EMAIL} to {RECIPIENT_EMAIL}")
        return jsonify({"message": "Email sent successfully."}), 200
    except Exception as e:
        email_sending_status.labels(status="failure").inc()
        logging.error(f"Failed to send email: {e}")
        return jsonify({"message": "Failed to send email.", "error": str(e)}), 500

@app.route('/slack/events', methods=['POST'])
def slack_events():
    """Handle Slack events."""
    if IS_TESTING:
        return jsonify({"message": "Slack events are mocked in test mode."}), 200
    return slack_handler.handle(request)

@app.route('/')
def home():
    return "AI-Powered Alerting System is running."

@app.route('/metrics')
def metrics():
    """Expose Prometheus metrics."""
    return Response(generate_latest(), content_type="text/plain")

@slack_app.command("/alert")
def alert_command(ack, respond, command):
    """Respond to Slack command with a log alert."""
    ack()
    log_message = command.get("text", "No message provided")
    severity = classify_log_event(log_message)
    respond(f"Log message classified as {severity}: {log_message}")

if __name__ == '__main__':
    logging.info("Starting Prometheus metrics server on port 8000...")
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
