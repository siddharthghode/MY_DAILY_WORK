from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# MinIO endpoint URL for local dev if not explicitly set
if not AWS_S3_ENDPOINT_URL:
    AWS_S3_ENDPOINT_URL = 'http://localhost:9000'
