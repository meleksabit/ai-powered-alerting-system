from unittest.mock import patch, MagicMock
from my_app.app import app

def test_home_page():
    """Test the home page endpoint."""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"AI-Powered Alerting System is running." in response.data

def test_metrics_endpoint():
    """Test the Prometheus metrics endpoint."""
    client = app.test_client()
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b"# HELP" in response.data

@patch("yagmail.SMTP")
def test_email_sending(mock_smtp):
    """Test successful email sending."""
    mock_yag = mock_smtp.return_value
    mock_yag.send.return_value = None
    client = app.test_client()
    response = client.get('/send_email/test_message')
    assert response.status_code == 200
    assert b"Email sent successfully." in response.data

@patch("yagmail.SMTP")
def test_email_sending_failure(mock_smtp):
    """Test email sending failure."""
    mock_smtp.return_value.send.side_effect = Exception("SMTP error")
    client = app.test_client()
    response = client.get('/send_email/test_message')
    assert response.status_code == 500
    assert b"Failed to send email." in response.data

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
