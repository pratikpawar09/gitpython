

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7!-*6ouwty-6j-08czqioy8yjxl4#_j!6v+@(x^g(@vc-&+3g5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appone',
    'rest_framework',  # to provid rest apis
    'rest_framework_swagger', # for uris -- request/response formats -documentation
    #'rest_auth',
    'rest_framework.authtoken',#for security purpose --> make sure u perform -- migrate --> to create table
]                               # authtoken_token ---> to store user tokens

# 1Basic Authentication --> client --use--> username/password
# 2Token Authentication --> initially client -- username/password --> server--> Token -->thereafter client use --> token for communication
# 3Session Authentication --> every login -->username/password -->server-- will generate the token --> session-->
                        # within that session --> user will send token--> once session is expired--> that token wont work

                        # next login --> username/password --> will generate token -> and so on

#Security -->                   #basic                #tk       #stkn
        # 1Authentication -->  username/password --> token --> session token --> Authenticated
                             #admin -admin13 --> x --> Auth
                             #guest guest123 --> y --> Auth
                             #clerk clerk123 --> z --> Auth
        # 2Authorization  --> permissions -- roles and responsibilities
                            #x --> all      --> diff
                            #y --> only read permission -
                            #z ---> read/modify/add ---> cannot delete/drop

#from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BaseAuthentication
#from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly

# IsAuthenticated --> valid token <-- valid username/password --> createuser --> normal/admin
#IsAdmin          --> valid token <-- valid username/password -->createuser ---> admin

    # valid -- guest/clerk --> only admin cha --> token

# crud -- > student--> 6             crud--  Emp    --> 6

REST_FRAMEWORK = {
    #latest drf - version -- swagger --> compatibility issue
    'DEFAULT_SCHEMA_CLASS':'rest_framework.schemas.coreapi.AutoSchema',
    #I want rest apis to be secured with token -->2 --> user --> server [username/password] --> Token -
    'DEFAULT_AUTHENTICATION_CLASSES': [
                                       'rest_framework.authentication.TokenAuthentication',
                                       # 'rest_framework.authentication.SessionAuthentication',
                                       # 'rest_framework.authentication.BaseAuthentication',
                                       ],

    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',]
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djsecurity.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'djsecurity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pydb',
        'HOST' : 'localhost',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'root'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
