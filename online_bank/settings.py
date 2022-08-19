"""
Django settings for online_bank project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nc@ty7fx4rv2a8j7nkd-7$d1$^-s$5o#37b!6qv0uh@nok$c2o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

TEST_MODE = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Users.apps.UsersConfig',
    'wallet.apps.WalletConfig',
    'company.apps.CompanyConfig',
    'core.apps.CoreConfig',
     #3rdparty
    #'whitenoise.runserver_nostatic',
    'crispy_forms', 
    'djmoney'
    #'phonenumber_field',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
     #whitenoise
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #language translation   
    #'django.middleware.locale.LocalMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'online_bank.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
            os.path.join(BASE_DIR,'Users/templates/dashboard'),
            os.path.join(BASE_DIR,'templates/email'),
            os.path.join(BASE_DIR,'templates/registration'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'core.context.core',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'online_bank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation

# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = 'dashboard'

LOGOUT_REDIRECT_URL = "index"

AUTH_USER_MODEL = 'Users.User'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

#LANGUAGE_CODE = 'es'

LOCALE_PATHS = [
    os.path.join(BASE_DIR,'languages')
]

TIME_ZONE = 'UTC'

INTERNATIONAL_TRANSFER_CHARGE = 1

INTERNAL_TRANSFER_CHARGE = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

MEDIA_URL = '/media/'

 
MEDIA_ROOT = os.path.join(BASE_DIR,"media")


STATICFILES_DIRS = [
os.path.join(BASE_DIR,"static")
]

STATIC_ROOT = os.path.join(BASE_DIR,"asset")

STATIC_URL = '/static/'

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#TWILLO
TWILLO_ACCOUNT_SID =  'AC213bba1c05225bedc1ebccccd8dbd9e0' 

TWILLO_AUTH_TOKEN =   '8512ae91f275f2bf0c8bf864e61692f3'

SMS_PHONE_NUMBER =  '+19709866198'

#EMAIL FOR GMAIL
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'geeetech.inc@gmail.com'
#EMAIL_HOST_PASSWORD = 'oehfphhfktpoezyh'


#EMAIL FOR ZOHO
EMAIL_HOST  = "smtp.zoho.com"
EMAIL_HOST_USER_ALERT = "transactions@credofinancebank.com"
EMAIL_HOST_USER_SUPPORT = "support@credofinancebank.com"

#for other emails 
EMAIL_HOST_USER = "support@credofinancebank.com"
DEFAULT_FROM_EMAIL  = "support@credofinancebank.com"
EMAIL_HOST_PASSWORD = '#Shawler200'

EMAIL_PORT = "587"
EMAIL_USE_TLS = "True"
#EMAIL_USE_SSL = "False"



