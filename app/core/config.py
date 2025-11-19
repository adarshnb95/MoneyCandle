from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    market_data_api_key: Optional[str] = None
    market_data_provider: str = "alpha_vantage"

    class Config:
        env_file = ".env"


settings = Settings()
