DEBUG               = True
API_URL_PREFIX      = "/api"
HOST                = '0.0.0.0'
PORT                = 5000
FILE_STORAGE_PATH   = '/Users/kd/Workspace/python/face/data/input' #'/tmp/nginx'
ENABLE_CORS         = True

JWT_SECRET_KEY      = 'tarento@ai.com$'
JWT_ACCESS_TOKEN_EXPIRY_IN_MINS     = 5
JWT_REFRESH_TOKEN_EXPIRY_IN_DAYS    = 30
FACE_MATCHING_TOLERANCE             = 0.60000000

DATABASE_SAVE       = False
DATABASE_URI        = 'mongodb://localhost:27017'
DATABASE_NAME       = 'tarento_ai'

REDIS_HOSTNAME      = 'localhost'
REDIS_PORT          = 6379

SUPPORTED_UPLOAD_FILETYPES = ['application/msword',
'application/pdf',
'image/x-ms-bmp',
'image/jpeg',
'image/jpg',
'image/png',
'text/plain',
'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
'video/mp4',
'video/webm']