from .config import config
from .development import (
    DEBUG, API_URL_PREFIX, HOST,
    PORT, FILE_STORAGE_PATH, ENABLE_CORS,
    JWT_SECRET_KEY, JWT_ACCESS_TOKEN_EXPIRY_IN_MINS, JWT_REFRESH_TOKEN_EXPIRY_IN_DAYS,
    FACE_MATCHING_TOLERANCE, DATABASE_SAVE, DATABASE_URI, DATABASE_NAME,
    REDIS_HOSTNAME, REDIS_PORT, SUPPORTED_UPLOAD_FILETYPES
)