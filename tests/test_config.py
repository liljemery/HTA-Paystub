from config.settings import Settings
import pytest
from dotenv import load_dotenv

def test_settings_loading(mock_env):
    """Test that Settings class loads environment variables correctly"""
    # load_dotenv(override=True)
    
    # global settings  
    settings = Settings()  

    assert settings.API_USER == "admin"
    assert settings.API_PASSWORD == "password"
    assert settings.EMAIL_HOST == "smtp.gmail.com"
    assert settings.EMAIL_PORT == 465 
    assert settings.EMAIL_USER == "jeremytesting60@gmail.com"
    assert settings.EMAIL_PASS == "scly etsu kdsx avpp"