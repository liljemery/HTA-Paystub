import pytest
from fastapi.testclient import TestClient
from main import app
from dotenv import load_dotenv
import os

@pytest.fixture
def client():
    """Fixture to provide a FastAPI test client."""
    return TestClient(app)

@pytest.fixture
def test_csv(tmp_path):
    """Fixture to create a sample CSV file for testing."""
    csv_content = """full_name,email,position,health_discount_amount,social_discount_amount,taxes_discount_amount,other_discount_amount,gross_salary,gross_payment,net_payment,period
John Doe,johndoe@example.com,Engineer,100,50,200,25,5000,5200,4800,2025-01-01
Jane Smith,janesmith@example.com,Manager,120,60,250,30,6000,6300,5700,2025-01-01
"""
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text(csv_content)
    return str(csv_file)

@pytest.fixture
def mock_env(monkeypatch):
    """Fixture to mock environment variables"""
    monkeypatch.setenv("API_USER", "admin")
    monkeypatch.setenv("API_PASSWORD", "password")
    monkeypatch.setenv("EMAIL_HOST", "smtp.example.com")
    monkeypatch.setenv("EMAIL_PORT", "465")
    monkeypatch.setenv("EMAIL_USER", "jeremytesting60@gmail.com")
    monkeypatch.setenv("EMAIL_PASS", "scly etsu kdsx avpp")

    # Ensure dotenv loads with override
    load_dotenv(override=True)
