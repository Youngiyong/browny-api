import os

from dotenv import load_dotenv

from pathlib import Path

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT")
    MYSQL_DB: str = os.getenv("MYSQL_DB")
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"
    API_V1_STR: str = "/api/v1"
    CDN_BUCKET: str = os.getenv("CDN")
    S3_BUCKET: str = os.getenv("S3_BUCKET")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    S3_AWS_ACCESS_KEY_ID: str = os.getenv("S3_AWS_ACCESS_KEY_ID")
    S3_AWS_SECRET_ACCESS_KEY: str = os.getenv("S3_AWS_SECRET_ACCESS_KEY")


settings = Settings()