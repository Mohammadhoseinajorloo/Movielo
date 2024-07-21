import os

from dotenv import load_dotenv

load_dotenv(".env")


class Settings:
    APP_NAME = os.getenv("APP_NAME")


settings = Settings()
