"""Here data imports from the file '.env' of django project"""

import os

import dotenv

dotenv.load_dotenv()

PROJECT_DB = os.getenv(
    "PROJECT_DB", ""
)
PROJECT_USER = os.getenv(
    "PROJECT_USER", ""
)
PROJECT_PASSWORD = os.getenv(
    "PROJECT_PASSWORD", ""
)
PROJECT_HOST = os.getenv(
    "PROJECT_HOST", ""
)
PROJECT_PORT = os.getenv(
    "PROJECT_PORT", ""
)
PROJECT_PROTOCOL = os.getenv("PROJECT_PROTOCOL", "")
PROJECT_SECRET_KEY = os.getenv("PROJECT_SECRET_KEY", "")
TOKEN_TIME_MINUTE_EXPIRE = os.getenv("TOKEN_TIME_MINUTE_EXPIRE", "")