import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    KEDEBAH_API_URL = os.getenv('KEDEBAH_API_URL')
    TICKETING_TOOL_API_URL = os.getenv('TICKETING_TOOL_API_URL')
    API_KEY = os.getenv('API_KEY')
    
    # Database configuration
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    
    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False