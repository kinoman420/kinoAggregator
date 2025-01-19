import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    STORAGE_DIR = os.getenv("STORAGE_DIR", "uploads")

settings = Settings()
