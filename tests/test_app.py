from unittest.mock import patch, MagicMock
from app import app

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
    assert b"# HELP" in response.data  # Basic check for Prometheus format output

def test_email_endpoint():
    """Test the send_email endpoint with mocked environment variables and Yagmail."""
    with patch('os.getenv') as mock_env:
        # Mock environment variables
        mock_env.side_effect = lambda key: {
            "SENDER_EMAIL": "mock-sender@example.com",
            "RECIPIENT_EMAIL": "mock-recipient@example.com"
        }.get(key)

        # Mock the Yagmail.SMTP object
        with patch('yagmail.SMTP') as mock_yagmail:
            mock_yag = mock_yagmail.return_value
            mock_yag.send.return_value = None  # Mock sending email as successful
            
            client = app.test_client()
            response = client.get('/send_email/test_log_message')
            
            assert response.status_code == 200
            assert b"Email sent successfully." in response.data

def test_slack_command():
    """Test the Slack command endpoint with mocked Slack credentials."""
    with patch('os.getenv') as mock_env:
        # Mock environment variables
        mock_env.side_effect = lambda key: {
            "SLACK_BOT_TOKEN": "mock-slack-token",
            "SLACK_SIGNING_SECRET": "mock-signing-secret"
        }.get(key)

        # Mock Slack handler
        with patch('app.slack_handler') as mock_handler:
            mock_handler.handle.return_value = "Mocked Slack response"

            client = app.test_client()
            # Simulate a POST request to Slack events endpoint
            response = client.post('/slack/events', json={})
            assert response.status_code == 200
