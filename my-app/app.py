from transformers import pipeline
from prometheus_client import Counter, start_http_server, generate_latest
from flask import Flask, Response
import logging
import os

# Load Hugging Face's BERT model (sentiment analysis as a placeholder)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Initialize Flask app
app = Flask(__name__)

# Prometheus Counter for log severity metrics
log_severity = Counter('log_severity', 'Log severity levels classified by BERT', ['severity'])

def classify_log_event(log_message):
    """
    Classify log messages based on Hugging Face BERT model sentiment analysis.
    We will map positive sentiment to 'not critical' and negative sentiment to 'critical'.
    """
    result = classifier(log_message)
    
    # If the sentiment is POSITIVE, we treat the log as 'not critical'
    if result[0]['label'] == 'POSITIVE':
        severity = 'not_critical'
    # If the sentiment is NEGATIVE, we treat the log as 'critical'
    else:
        severity = 'critical'

    # Update Prometheus metric
    log_severity.labels(severity=severity).inc()

    # Log the result for visibility
    logging.info(f"Classified log '{log_message}' as {severity}")
    return severity

# Root route
@app.route('/')
def home():
    return "AI-Powered Alerting System is running."

# Serve favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')    

# Route to expose metrics to Prometheus
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

# Route to classify a log message
@app.route('/log/<message>')
def log_message(message):
    severity = classify_log_event(message)
    return f"Log classified as {severity}\n"

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
