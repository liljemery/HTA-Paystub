from services.email_sender import send_email
from unittest.mock import patch
import pytest
import os

@pytest.fixture
def test_pdf(tmp_path):
    """Creates a temporary PDF file for testing email sending."""
    pdf_path = tmp_path / "test.pdf"
    pdf_path.write_text("Fake PDF content")
    return str(pdf_path)

@patch("smtplib.SMTP_SSL")
def test_email_sending(mock_smtp, test_pdf):
    """Tests if emails are sent correctly."""
    employees = [{"full_name": "John Doe", "email": "johndoe@example.com"}]
    pdf_paths = [test_pdf]

    result = send_email(employees, pdf_paths)
    print("Result:", result)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["email"] == "johndoe@example.com"
    assert result[0]["status"] == "sent"
