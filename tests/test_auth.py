from api.security import authenticate_user
from fastapi.security import HTTPBasicCredentials
import pytest

def test_valid_authentication():
    """Tests valid API authentication."""
    credentials = HTTPBasicCredentials(username="admin", password="password")
    assert authenticate_user(credentials) == "admin"

def test_invalid_authentication():
    """Tests invalid API authentication."""
    credentials = HTTPBasicCredentials(username="wrong", password="wrong")
    with pytest.raises(Exception):
        authenticate_user(credentials)
