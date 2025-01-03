from unittest.mock import patch
import pytest

def test_start_app_import():
    """Test that start_app.py can be imported without errors."""
    import my_app.start_app  # Ensure no ImportError is raised

@patch("prometheus_client.start_http_server")
def test_start_prometheus(mock_start_http):
    """Test Prometheus server start."""
    from my_app.start_app import start_prometheus
    start_prometheus()
    mock_start_http.assert_called_once_with(8000)

@patch("gunicorn.app.base.BaseApplication.run")
def test_start_gunicorn(mock_run):
    """Test Gunicorn server start."""
    from my_app.start_app import start_gunicorn
    start_gunicorn()
    mock_run.assert_called_once()
