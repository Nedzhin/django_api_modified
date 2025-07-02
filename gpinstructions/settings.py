INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'rest_framework',
    'core',
    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

SECRET_KEY = 'dummy'
ROOT_URLCONF = 'gpinstructions.urls'
DEBUG = True
ALLOWED_HOSTS = []