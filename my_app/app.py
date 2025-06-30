import logging
from prometheus_client import start_http_server, Counter, generate_latest
from flask import Flask, Response, jsonify, request
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import os
import yagmail
from slack_bolt import App as SlackApp
from slack_bolt.adapter.flask import SlackRequestHandler
from unittest.mock import MagicMock
from flask_wtf.csrf import CSRFProtect
from pathlib import Path

# Enable logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)
csrf = CSRFProtect(app)

# Health check flags
app_startup_completed = False
app_ready = False

# Check if the app is running in test mode
IS_TESTING = os.getenv("FLASK_ENV") == "testing"

# Slack setup
if not IS_TESTING:
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
    if not SLACK_BOT_TOKEN or not SLACK_SIGNING_SECRET:
        raise EnvironmentError("Slack credentials are missing. Please set them.")
    slack_app = SlackApp(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)
    slack_handler = SlackRequestHandler(slack_app)
else:
    # Mock SlackApp and SlackRequestHandler for testing
    slack_app = MagicMock()
    slack_handler = MagicMock()

# Prometheus metrics
log_severity = Counter('log_severity', 'Count of log severities', ['severity'])
email_sending_status = Counter('email_sending_status', 'Status of email sending', ['status'])

# Preload labels
log_severity.labels(severity="critical")
log_severity.labels(severity="not_critical")

# Email setup
if not IS_TESTING:
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
    if not SENDER_EMAIL or not RECIPIENT_EMAIL:
        raise EnvironmentError("Email credentials are missing.")
else:
    # Mock email credentials for testing
    SENDER_EMAIL = "mock-sender@example.com"
    RECIPIENT_EMAIL = "mock-recipient@example.com"

# Variables to hold the model and tokenizer, initialized as None
model = tokenizer = classifier = None

def lazy_load_model():
    """Load transformer model and tokenizer only when needed."""
    global model, tokenizer, classifier, app_ready
    if model is None or tokenizer is None or classifier is None:
        logging.info("Loading model and tokenizer lazily...")

        MODEL_NAME = os.getenv("HF_MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english")
        MODEL_CACHE = os.getenv("MODEL_CACHE", str(Path.home() / ".cache" / "huggingface"))

        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=MODEL_CACHE)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, cache_dir=MODEL_CACHE)
        classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

        logging.info("Model and tokenizer loaded.")
    app_ready = True

def classify_log_event(log_message):
    """Classify log messages using Hugging Face DistilBERT model."""
    lazy_load_model()  # Ensure the model and tokenizer are loaded
    result = classifier(log_message)  # Use the classifier pipeline

    # Determine severity based on sentiment analysis result
    severity = 'not_critical' if result[0]['label'] == 'POSITIVE' else 'critical'
    log_severity.labels(severity=severity).inc()
    logging.info(f"Classified log '{log_message}' as {severity}")
    return severity

@app.route('/health', methods=['GET'])
def health():
    """Liveness Probe: Check if the app is running."""
    return "OK", 200

@app.route('/readiness', methods=['GET'])
def readiness():
    """Readiness Probe: Check if the app is ready to handle requests."""
    if app_ready:
        return "READY", 200
    return "NOT READY", 503

@app.route('/startup', methods=['GET'])
def startup():
    """Startup Probe: Check if the app has completed initialization."""
    if app_startup_completed:
        return "STARTUP COMPLETE", 200
    return "STARTING UP", 503

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
        logging.info(f"Email sent successfully from {SENDER_EMAIL}")
        return jsonify({"message": "Email sent successfully."}), 200
    except Exception as e:
        email_sending_status.labels(status="failure").inc()
        logging.error(f"Failed to send email: {e}")
        return jsonify({"message": "Failed to send email.", "error": str(e)}), 500

@app.route('/slack/events', methods=['POST'])
def slack_events():
    """Handle Slack events."""
    return slack_handler.handle(request)

@app.route('/')
def home(): return "AI-Powered Alerting System is running."

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
    # Start Prometheus metrics server on port 8000
    logging.info("Starting Prometheus metrics server on port 8000...")
    start_http_server(8000)

    # Mark startup as complete before running the Flask app
    app_startup_completed = True

    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
