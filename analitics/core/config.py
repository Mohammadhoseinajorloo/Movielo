import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME")
    DATA_DIR = os.getenv("DATA_DIR")


settings = Settings()
