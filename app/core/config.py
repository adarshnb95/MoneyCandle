from pydantic import BaseSettings

class Settings(BaseSettings):
    market_data_api_key: str | None = None
    market_data_provider: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
