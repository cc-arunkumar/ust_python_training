from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = Field(default="UST Task Manager", alias="APP_NAME")
    env: str = Field(default="development", alias="ENV")
    debug: bool = Field(default=True, alias="DEBUG")
    secret_key: str = Field(alias="SECRET_KEY")
    algorithm: str = Field(default="HS256", alias="ALGORITHM")
    access_token_expire_minutes: int = Field(default=60, alias="ACCESS_TOKEN_EXPIRE_MINUTES")

    mysql_user: str = Field(alias="MYSQL_USER")
    mysql_password: str = Field(alias="MYSQL_PASSWORD")
    mysql_host: str = Field(alias="MYSQL_HOST")
    mysql_port: int = Field(alias="MYSQL_PORT")
    mysql_db: str = Field(alias="MYSQL_DB")

    mongo_uri: str = Field(alias="MONGO_URI")
    mongo_db: str = Field(alias="MONGO_DB")

    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    log_sql: bool = Field(default=True, alias="LOG_SQL")

    file_upload_dir: str = Field(default="./uploads", alias="FILE_UPLOAD_DIR")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        populate_by_name = True

settings = Settings()
