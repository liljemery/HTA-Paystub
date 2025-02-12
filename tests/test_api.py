import pytest
from fastapi.testclient import TestClient
from config.settings import settings

def test_api_authentication(client):
    """Tests if API authentication works correctly."""
    response = client.post("/process", data={"country": "do", "company_name": "atdev"})
    assert response.status_code == 401  # Unauthorized

def test_process_paystubs(client, test_csv):
    """Tests paystub processing via API."""
    with open(test_csv, "rb") as file:
        response = client.post(
            "/process",
            files={"file": file},
            data={"country": "do", "company_name": "atdev"},
            auth=(settings.API_USER, settings.API_PASSWORD)
        )
    
    assert response.status_code == 200
    assert "emails_sent" in response.json()
