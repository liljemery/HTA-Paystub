import sys
import os
import pytest
from fastapi.testclient import TestClient

# Ensure the root directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from main import app  # Import after modifying sys.path

@pytest.fixture
def client():
    """Creates a test client for FastAPI."""
    return TestClient(app)

@pytest.fixture
def test_csv(tmp_path):
    """Creates a sample payroll CSV file for testing."""
    csv_content = """full_name,email,position,health_discount_amount,social_discount_amount,
taxes_discount_amount,other_discount_amount,gross_salary,gross_payment,
net_payment,period
John Doe,johndoe@example.com,Developer,500,300,200,100,5000,4800,4500,2024-01-01
Jane Smith,janesmith@example.com,Designer,400,250,150,50,4000,3800,3500,2024-01-01"""
    
    file_path = tmp_path / "test_payroll.csv"
    with open(file_path, "w") as f:
        f.write(csv_content)
    
    return str(file_path)  # Return file path as string
