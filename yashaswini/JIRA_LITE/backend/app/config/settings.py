from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mysql_host: str
    mysql_user: str
    mysql_password: str
    mysql_db: str

    mongo_uri: str
    mongo_db: str

    class Config:
        env_file = ".env"


settings = Settings()



