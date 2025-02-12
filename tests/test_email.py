from services.email_sender import send_email
from unittest.mock import patch

@patch("smtplib.SMTP")
def test_email_sending(mock_smtp):
    """Tests if emails are sent correctly."""
    employees = [{"full_name": "John Doe", "email": "johndoe@example.com"}]
    pdf_paths = ["test.pdf"]
    
    result = send_email(employees, pdf_paths)

    assert len(result) == 1
    assert result[0]["email"] == "johndoe@example.com"
    assert result[0]["status"] == "sent"
