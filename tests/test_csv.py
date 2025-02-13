import pytest
from services.file_processor import process_csv

def test_csv_processing(test_csv):
    """Tests if CSV is correctly processed into employee data."""
    employees = process_csv(test_csv)

    assert len(employees) == 2
    assert employees[0]["full_name"] == "John Doe"
    assert employees[0]["email"] == "johndoe@example.com"
    assert employees[0]["gross_salary"] == 5000
