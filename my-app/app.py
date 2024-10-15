from flask import Flask, send_from_directory, Response
from prometheus_client import Counter, start_http_server, generate_latest
from transformers import pipeline
import logging
import os

# Load Hugging Face's BERT model
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Initialize Flask app
app = Flask(__name__)

# Prometheus Counter for log severity
log_severity = Counter('log_severity', 'Log severity levels classified by BERT', ['severity'])

def classify_log_event(log_message):
    result = classifier(log_message)
    severity = 'critical' if result[0]['label'] == 'POSITIVE' else 'not_critical'
    log_severity.labels(severity=severity).inc()
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

# Expose Prometheus metrics
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

# Log classification route
@app.route('/log/<message>')
def log_message(message):
    severity = classify_log_event(message)
    return f"Log classified as {severity}\n"

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus metrics available on port 8000
    app.run(host='0.0.0.0', port=5000)  # Flask app available on port 5000
