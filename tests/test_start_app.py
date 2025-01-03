from unittest.mock import patch, MagicMock
from my_app import start_app
import pytest

@patch("prometheus_client.start_http_server")
def test_start_prometheus(mock_start_http):
    from my_app.start_app import start_prometheus
    start_prometheus()
    mock_start_http.assert_called_once_with(8000)
