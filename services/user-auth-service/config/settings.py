from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "User Auth Service"
    debug: bool = True
    database_url: str

    company_email_domain: str
    otp_hmac_secret: str
    otp_expiry_minutes: int = 5
    otp_max_attempts: int = 5
    otp_resend_cooldown_seconds: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # prevents crashes if .env has extra variables
    )


settings = Settings()
