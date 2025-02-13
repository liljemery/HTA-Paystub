import pytest
import os
from services.pdf_generator import generate_pdf

@pytest.fixture
def payroll_data():
    """Fixture to provide payroll data for testing."""
    return [
        {
            "full_name": "John Doe",
            "email": "johndokidoki11@yopmail.com",
            "position": "Developer",
            "health_discount_amount": 500,
            "social_discount_amount": 300,
            "taxes_discount_amount": 200,
            "other_discount_amount": 100,
            "gross_salary": 5000,
            "gross_payment": 4800,
            "net_payment": 4500,
            "period": "2024-01-01",
        },
        {
            "full_name": "Jane Smith",
            "email": "janesmithers11@yopmail.com",
            "position": "Designer",
            "health_discount_amount": 400,
            "social_discount_amount": 250,
            "taxes_discount_amount": 150,
            "other_discount_amount": 50,
            "gross_salary": 4000,
            "gross_payment": 3800,
            "net_payment": 3500,
            "period": "2024-01-01",
        }
    ]

def test_pdf_generation(payroll_data):
    """Tests if PDFs are generated correctly from payroll data."""
    pdf_files = generate_pdf(payroll_data, "do", "atdev")

    assert len(pdf_files) == len(payroll_data), "PDF count mismatch!"

    for pdf in pdf_files:
        assert pdf.endswith(".pdf"), f"File {pdf} is not a PDF!"
        assert os.path.exists(pdf), f"PDF file {pdf} does not exist!"
