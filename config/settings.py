import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    API_USER = os.getenv("API_USER", "admin")
    API_PASSWORD = os.getenv("API_PASSWORD", "password")
    EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.example.com")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", 465))
    EMAIL_USER = os.getenv("EMAIL_USER", "no-reply@example.com")
    EMAIL_PASS = os.getenv("EMAIL_PASS", "emailpassword")
    COMPANY_NAME = os.getenv("COMPANY_NAME", "atdev")

settings = Settings()
