from unittest.mock import patch, MagicMock
import my_app.start_app
import pytest

@patch("prometheus_client.start_http_server")
def test_start_prometheus(mock_start_http):
    """Test Prometheus server start."""
    my_app.start_app.start_prometheus()
    mock_start_http.assert_called_once_with(8000)
