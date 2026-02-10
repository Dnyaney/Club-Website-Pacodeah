import os
import dj_database_url # Make sure to pip install this
from pathlib import Path

# ... (BASE_DIR remains the same)

# SECURITY: Get key from environment or use a dummy for local dev
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-local-key')

# SECURITY: Never run with debug on in production
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Railway provides the domain, but we'll allow all railway apps and localhost
ALLOWED_HOSTS = ['*'] 
if os.environ.get('RAILWAY_STATIC_URL'):
    ALLOWED_HOSTS.append(os.environ.get('RAILWAY_STATIC_URL'))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pacodeah',
    'whitenoise.runserver_nostatic', # Add this for better static handling
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # REQUIRED for Railway
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ... (TEMPLATES and WSGI remain same)

# Database: Use DATABASE_URL from Railway, fallback to SQLite for local work
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}

# ... (Password validators and i18n remain same)

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # New line: where files go on collectstatic
STATICFILES_DIRS = [BASE_DIR / 'static']

# This tells WhiteNoise to compress and cache your files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# CSRF Settings for production
CSRF_TRUSTED_ORIGINS = ['https://*.railway.app']