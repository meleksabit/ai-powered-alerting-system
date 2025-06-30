import os
import logging
from prometheus_client import start_http_server
import gunicorn.app.base

# Import app and model loader
from my_app.app import app, lazy_load_model
from my_app import app as flask_module

# Preload the model to avoid lazy-load delay during first request
lazy_load_model()

# Set readiness flag after model is loaded
flask_module.app_ready = True
flask_module.app_startup_completed = True

def start_prometheus():
    logging.info("Starting Prometheus metrics server on port 8000...")
    start_http_server(8000)

class StandaloneApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def start_gunicorn():
    logging.info("Starting Gunicorn server on port 5000...")
    options = {
        'bind': '0.0.0.0:5000',
        'workers': 1,
        'timeout': 120,
        'worker_class': 'sync',
    }
    StandaloneApplication(app, options).run()

# Main entry point
if __name__ == "__main__":
    # Start Prometheus metrics server first
    start_prometheus()
    
    # Start Gunicorn to serve Flask app
    start_gunicorn()
