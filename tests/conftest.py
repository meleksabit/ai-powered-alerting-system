import pytest
from unittest.mock import patch
from my_app.app import app

@pytest.fixture
def client():
    """Create a Flask test client."""
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_prometheus():
    """Mock Prometheus server."""
    with patch("prometheus_client.start_http_server") as mock_start_http:
        yield mock_start_http

@pytest.fixture
def mock_yagmail():
    """Mock Yagmail SMTP client."""
    with patch("yagmail.SMTP") as mock_smtp:
        yield mock_smtp

@pytest.fixture
def mock_classify():
    """Mock classify_log_event function."""
    with patch("my_app.app.classify_log_event", return_value="critical") as mock_func:
        yield mock_func
