"""Here data imports from the file '.env' of django project"""

import os

import dotenv

dotenv.load_dotenv()

PROJECT_HOST = os.getenv(
    "PROJECT_HOST", ""
)
PROJECT_PORT = os.getenv(
    "PROJECT_PORT", ""
)
PROJECT_PROTOCOL = os.getenv("PROJECT_PROTOCOL", "")
PROJECT_SECRET_KEY = os.getenv("PROJECT_SECRET_KEY", "")
TOKEN_TIME_MINUTE_EXPIRE = os.getenv("TOKEN_TIME_MINUTE_EXPIRE", "")
API_URL = os.getenv("API_URL", "")
API_KEY = os.getenv("API_KEY", "")
PHONE_SEND = os.getenv("PHONE_SEND", "")