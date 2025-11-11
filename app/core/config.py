from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "SBFC Smart Loan Management System"
    DEBUG: bool = False

    DATABASE_URL: str = "sqlite:///./sbfc_smart_loan.db"

    SECRET_KEY: str = "super-secure-sbfc-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    OTP_EXPIRE_MINUTES: int = 10
    OTP_LENGTH: int = 6

    SMTP_HOST: Optional[str] = None
    SMTP_PORT: Optional[int] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: Optional[str] = None

    SMS_API_KEY: Optional[str] = None
    SMS_API_URL: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
