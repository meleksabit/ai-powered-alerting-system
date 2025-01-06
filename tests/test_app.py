import pytest

def test_home_page(client):
    """Test the home page endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"AI-Powered Alerting System is running." in response.data

def test_metrics_endpoint(client):
    """Test the Prometheus metrics endpoint."""
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b"# HELP" in response.data

def test_email_sending(client, mock_yagmail, mock_classify):
    """Test successful email sending."""
    mock_yag = mock_yagmail.return_value
    mock_yag.send.return_value = None

    response = client.get('/send_email/test_message')

    assert response.status_code == 200
    assert b"Email sent successfully." in response.data
    mock_classify.assert_called_once_with("test_message")

def test_email_sending_failure(client, mock_yagmail, mock_classify):
    """Test email sending failure."""
    mock_yagmail.return_value.send.side_effect = Exception("SMTP error")

    response = client.get('/send_email/test_message')

    assert response.status_code == 500
    assert b"Failed to send email." in response.data
    mock_classify.assert_called_once_with("test_message")
