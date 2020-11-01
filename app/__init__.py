from flask import Flask

app = Flask(__name__)

MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS= (os.path.join(PROJECT_ROOT,'static'),)

from app import views

