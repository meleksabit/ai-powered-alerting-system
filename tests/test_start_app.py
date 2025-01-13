from unittest.mock import patch

def test_start_prometheus(mock_prometheus):
    """Test Prometheus server start."""
    from my_app.start_app import start_prometheus
    start_prometheus()
    mock_prometheus.assert_called_once_with(8000)

@patch("gunicorn.app.base.BaseApplication.run")
def test_start_gunicorn(mock_run):
    """Test Gunicorn server start."""
    from my_app.start_app import start_gunicorn
    start_gunicorn()
    mock_run.assert_called_once()
