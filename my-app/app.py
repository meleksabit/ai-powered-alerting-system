import logging
from prometheus_client import start_http_server, Counter, generate_latest
from flask import Flask, Response, jsonify
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import os
import yagmail

# Enable logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Define Prometheus Counters
log_severity = Counter('log_severity', 'Count of log severities', ['severity'])
email_sending_status = Counter('email_sending_status', 'Status of email sending', ['status'])

# Load email credentials from environment variables or Docker secrets
try:
    # Check if secrets are provided through Docker secrets
    with open("/run/secrets/email_address", "r") as f:
        SENDER_EMAIL = f.read().strip()
    with open("/run/secrets/notification_receiver", "r") as f:
        RECIPIENT_EMAIL = f.read().strip()
except FileNotFoundError:
    # Fallback to environment variables if Docker secrets are not used
    SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")
    RECIPIENT_EMAIL = os.getenv("NOTIFICATION_RECEIVER")

# Validate email configuration
if not SENDER_EMAIL or not RECIPIENT_EMAIL:
    raise EnvironmentError("Email credentials are missing. Please set them using Docker secrets or environment variables.")

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
    """
    Classify log messages using Hugging Face DistilBERT model for sentiment analysis.
    Lazily loads the model and tokenizer if they are not already loaded.
    """
    lazy_load_model()

    result = classifier(log_message)

    # Determine severity based on sentiment
    if result[0]['label'] == 'POSITIVE':
        severity = 'not_critical'
    else:
        severity = 'critical'

    log_severity.labels(severity=severity).inc()

    logging.info(f"Classified log '{log_message}' as {severity}")
    return severity

@app.route('/send_email/<log_message>')
def send_email_endpoint(log_message):
    """
    Sends an email containing the classified log message.
    """
    try:
        severity = classify_log_event(log_message)

        # Initialize Yagmail
        yag = yagmail.SMTP(SENDER_EMAIL)

        # Email Content
        subject = "Log Alert: New Event Notification"
        body = f"Log Message: {log_message}\nSeverity: {severity}"

        # Send Email
        yag.send(to=RECIPIENT_EMAIL, subject=subject, contents=body)

        # Prometheus metric and logging
        email_sending_status.labels(status="success").inc()
        logging.info(f"Email sent successfully from {SENDER_EMAIL} to {RECIPIENT_EMAIL}")

        return jsonify({"message": "Email sent successfully."}), 200
    except Exception as e:
        # Prometheus metric and logging for failure
        email_sending_status.labels(status="failure").inc()
        logging.error(f"Failed to send email: {e}")

        return jsonify({"message": "Failed to send email.", "error": str(e)}), 500

@app.route('/')
def home():
    return "AI-Powered Alerting System is running."

@app.route('/metrics')
def metrics():
    """Expose Prometheus metrics."""
    return Response(generate_latest(), content_type="text/plain")

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    logging.info("Starting Prometheus metrics server on port 8000...")
    start_http_server(8000)

    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
