import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    DATABASE_URL = "sqlite:///database.db"  # Changed to local SQLite file
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")
    API_VERSION = os.getenv("API_VERSION", "v1")
    
    # Example of additional settings
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 20))  # Max file size in MB for uploads
    
    def __str__(self):
        return f"Settings: {self.__dict__}"

settings = Settings()