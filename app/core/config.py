from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.

    Values can be overridden using environment variables
    or a local .env file.
    """

    APP_NAME: str = "Medical AI Serving Platform"

    VERSION: str = "0.1.0"

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    DEBUG: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()