import os
import logging
from prometheus_client import start_http_server
import gunicorn.app.base

# Define the Flask app entry point (import from your Flask app)
from my_app.app import app

# Start Prometheus metrics server before starting Gunicorn
def start_prometheus():
    """Start Prometheus metrics server on port 8000."""
    logging.info("Starting Prometheus metrics server on port 8000...")
    print("DEBUG: start_prometheus called")
    start_http_server(8000)

# Class to start Gunicorn within Python
class StandaloneApplication(gunicorn.app.base.BaseApplication):
    """Standalone Gunicorn application."""

    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        """Load Gunicorn configuration."""
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        """Load the application."""
        return self.application

# Function to start the Flask app with Gunicorn
def start_gunicorn():
    """Start the Flask app using Gunicorn."""
    logging.info("Starting Gunicorn server on port 5000...")
    options = {
        'bind': '0.0.0.0:5000',
        'workers': 4,  # Number of worker processes
        'timeout': 30,  # Increase timeout to avoid premature worker timeouts
    }
    StandaloneApplication(app, options).run()

# Main entry point
if __name__ == "__main__":
    # Start Prometheus metrics server first
    start_prometheus()
    
    # Start Gunicorn to serve Flask app
    start_gunicorn()
