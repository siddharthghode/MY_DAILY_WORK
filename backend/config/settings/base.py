import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env if present
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'insecure-django-secret-key-change-in-production')
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() in ('true', '1', 't')

ALLOWED_HOSTS = [host.strip() for host in os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',') if host.strip()]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party
    'rest_framework',
    'drf_spectacular',
    
    # Local apps
    'apps.accounts.apps.AccountsConfig',
    'apps.files.apps.FilesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# Database Configuration
DB_ENGINE = os.getenv('DB_ENGINE', 'django.db.backends.sqlite3')
if DB_ENGINE == 'django.db.backends.sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / os.getenv('DB_NAME', 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': DB_ENGINE,
            'NAME': os.getenv('DB_NAME', 'object_storage_db'),
            'USER': os.getenv('DB_USER', 'storage_user'),
            'PASSWORD': os.getenv('DB_PASSWORD', 'storage_password'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# DRF Spectacular OpenAPI documentation
SPECTACULAR_SETTINGS = {
    'TITLE': 'Object Storage & File Management API',
    'DESCRIPTION': 'Production-grade S3-compatible Object Storage System with DRF',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# S3 / MinIO Object Storage Configuration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'minioadmin')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'minioadmin')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME', 'my-storage-bucket')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME', 'us-east-1')
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL', None)
AWS_DEFAULT_ACL = os.getenv('AWS_DEFAULT_ACL', 'private')
AWS_S3_SIGNATURE_VERSION = os.getenv('AWS_S3_SIGNATURE_VERSION', 's3v4')

# Limits & Storage Policies
UPLOAD_MAX_FILE_SIZE_BYTES = int(os.getenv('UPLOAD_MAX_FILE_SIZE_BYTES', 5 * 1024 * 1024 * 1024))  # 5 GB
BACKEND_MEDIATED_MAX_BYTES = int(os.getenv('BACKEND_MEDIATED_MAX_BYTES', 10 * 1024 * 1024))         # 10 MB
DEFAULT_PART_SIZE_BYTES = int(os.getenv('DEFAULT_PART_SIZE_BYTES', 10 * 1024 * 1024))              # 10 MB
MIN_PART_SIZE_BYTES = int(os.getenv('MIN_PART_SIZE_BYTES', 5 * 1024 * 1024))                       # 5 MB
MAX_PART_COUNT = 10000
PRESIGNED_URL_EXPIRY_SECONDS = int(os.getenv('PRESIGNED_URL_EXPIRY_SECONDS', 3600))                # 1 hour
DOWNLOAD_URL_EXPIRY_SECONDS = int(os.getenv('DOWNLOAD_URL_EXPIRY_SECONDS', 900))                   # 15 minutes

# CDN Settings
CDN_BASE_URL = os.getenv('CDN_BASE_URL', '')

# Celery & Redis
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} [{name}:{lineno}] {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': os.getenv('LOG_LEVEL', 'INFO'),
    },
    'loggers': {
        'apps.files': {
            'handlers': ['console'],
            'level': os.getenv('LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
