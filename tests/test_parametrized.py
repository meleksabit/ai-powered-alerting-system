import pytest

@pytest.mark.parametrize(
    "log_message, expected_status, mock_side_effect, expected_response",
    [
        ("test_message", 200, None, b"Email sent successfully."),
        ("test_message", 500, Exception("SMTP error"), b"Failed to send email."),
    ],
)
def test_email_sending_cases(client, mock_yagmail, mock_classify, log_message, expected_status, mock_side_effect, expected_response):
    """Test multiple scenarios for email sending."""
    mock_yag = mock_yagmail.return_value
    mock_yag.send.side_effect = mock_side_effect

    response = client.get(f'/send_email/{log_message}')

    assert response.status_code == expected_status
    assert expected_response in response.data
    mock_classify.assert_called_once_with(log_message)
