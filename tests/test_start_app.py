from unittest.mock import patch
import pytest

@patch("prometheus_client.start_http_server")
def test_start_prometheus(mock_start_http):
    """Test Prometheus server startup."""
    from my_app.start_app import start_prometheus  # Import only this function
    start_prometheus()
    mock_start_http.assert_called_once_with(8000)

@patch("gunicorn.app.base.BaseApplication.run")
def test_start_gunicorn(mock_run):
    """Test Gunicorn server startup."""
    from my_app.start_app import start_gunicorn
    start_gunicorn()
    mock_run.assert_called_once()
