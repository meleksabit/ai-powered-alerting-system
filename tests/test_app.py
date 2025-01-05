from unittest.mock import patch, MagicMock
from my_app.app import app
import my_app.start_app
import pytest

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
    assert b"# HELP" in response.data  # Verify Prometheus format output

@patch("my_app.app.classify_log_event", return_value="critical")
@patch("yagmail.SMTP")
def test_email_sending(mock_smtp, mock_classify):
    """Test successful email sending."""
    mock_yag = mock_smtp.return_value
    mock_yag.send.return_value = None

    client = app.test_client()
    response = client.get('/send_email/test_message')

    assert response.status_code == 200
    assert b"Email sent successfully." in response.data

    # Assert classify_log_event was called with the correct arguments
    mock_classify.assert_called_once_with("test_message")

@patch("my_app.app.classify_log_event", return_value="critical")
@patch("yagmail.SMTP")
def test_email_sending_failure(mock_smtp, mock_classify):
    """Test email sending failure."""
    mock_smtp.return_value.send.side_effect = Exception("SMTP error")

    client = app.test_client()
    response = client.get('/send_email/test_message')

    assert response.status_code == 500
    assert b"Failed to send email." in response.data

    # Assert classify_log_event was called even in case of email failure
    mock_classify.assert_called_once_with("test_message")

@patch("prometheus_client.start_http_server")
def test_start_prometheus(mock_start_http):
    assert mock_start_http is not None, "Mocking failed for prometheus_client.start_http_server"
    from my_app.start_app import start_prometheus
    start_prometheus()
    mock_start_http.assert_called_once_with(8000)

@patch("gunicorn.app.base.BaseApplication.run")
def test_start_gunicorn(mock_run):
    """Test Gunicorn server start."""
    from my_app.start_app import start_gunicorn
    start_gunicorn()
    mock_run.assert_called_once()
