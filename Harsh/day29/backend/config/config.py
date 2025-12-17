from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    MYSQL_DB_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    MONGODB_URL: str
    MONGODB_DATABASE: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

Config = get_settings()