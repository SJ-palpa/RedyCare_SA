from .base import *

DEBUG = False
ALLOWED_HOSTS = ['redycare.ch', 'www.redycare.ch','redycare.com','www.redycare.ch','redy.care','www.redy.care']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'redycarDB',
        'USER': 'amorAssociation',
        'PASSWORD': 'Amv7kc2nM5QuDnLd',
        'HOST': 'amorAssociation.mysql.pythonanywhere-services.com',
        'PORT': ''
    }
}

#STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
#STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')