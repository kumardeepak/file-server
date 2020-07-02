import logging
import os
import configs
from configs import development as dev_config

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)



def config():
    return {
        "DEBUG" : os.getenv("DEBUG", dev_config.DEBUG),
        "API_URL_PREFIX" : "/api",
        "HOST" : '0.0.0.0',
        "PORT" : os.getenv("PORT", dev_config.PORT),
        "FILE_STORAGE_PATH" : os.getenv("FILE_STORAGE_PATH", dev_config.FILE_STORAGE_PATH),
        "ENABLE_CORS" : os.getenv("ENABLE_CORS", dev_config.ENABLE_CORS),
        "JWT_SECRET_KEY" : os.getenv("JWT_SECRET_KEY", dev_config.JWT_SECRET_KEY),
        "JWT_ACCESS_TOKEN_EXPIRY_IN_MINS" : os.getenv("JWT_ACCESS_TOKEN_EXPIRY_IN_MINS", dev_config.JWT_ACCESS_TOKEN_EXPIRY_IN_MINS),
        "JWT_REFRESH_TOKEN_EXPIRY_IN_DAYS" : os.getenv("JWT_REFRESH_TOKEN_EXPIRY_IN_DAYS", dev_config.JWT_REFRESH_TOKEN_EXPIRY_IN_DAYS),
        "FACE_MATCHING_TOLERANCE" : os.getenv("FACE_MATCHING_TOLERANCE", dev_config.FACE_MATCHING_TOLERANCE),
        "REDIS_HOSTNAME"   : os.getenv("REDIS_HOSTNAME", dev_config.REDIS_HOSTNAME),
        "REDIS_PORT" : os.getenv("REDIS_PORT", dev_config.REDIS_PORT),
        "SUPPORTED_UPLOAD_FILETYPES" : os.getenv("SUPPORTED_UPLOAD_FILETYPES", dev_config.SUPPORTED_UPLOAD_FILETYPES),
    }