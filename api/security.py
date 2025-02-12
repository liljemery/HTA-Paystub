from fastapi import HTTPException, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from config.settings import settings

security = HTTPBasic()

def authenticate_user(credentials: HTTPBasicCredentials = Security(security)):
    """Authenticate user using environment variables."""
    if credentials.username != settings.API_USER or credentials.password != settings.API_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username
