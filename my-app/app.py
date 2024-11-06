import logging
from prometheus_client import start_http_server, Counter, generate_latest
from flask import Flask, send_from_directory, Response
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import os

# Enable logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Define a Prometheus Counter to track the severity of logs
log_severity = Counter('log_severity', 'Count of log severities', ['severity'])

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

@app.route('/')
def home():
    return "AI-Powered Alerting System is running."

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')    

@app.route('/log/<message>')
def log_message(message):
    severity = classify_log_event(message)
    return f"Log classified as {severity}\n"

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    logging.info("Starting Prometheus metrics server on port 8000...")
    start_http_server(8000)
    
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
