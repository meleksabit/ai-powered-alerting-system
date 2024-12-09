from unittest.mock import patch
from app import app

def test_home_page():
    with patch.dict('os.environ', {"SLACK_BOT_TOKEN": "test-token", "SLACK_SIGNING_SECRET": "test-secret"}):
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200
        assert b"AI-Powered Alerting System is running." in response.data
