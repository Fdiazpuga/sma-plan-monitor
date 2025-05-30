"""
Django settings for ppda_core project.

Generated by 'django-admin startproject' using Django 5.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from dotenv import load_dotenv
from pathlib import Path
from decouple import config
import dj_database_url
from pathlib import Path

load_dotenv('.env')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Database variables
dbname = os.getenv('DB_NAME')
dbuser = os.getenv('DB_USER')
dbpass = os.getenv('DB_PASSWORD')
dbhost = os.getenv('DB_HOST')
dbport = os.getenv('DB_PORT')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #librerias
    'rest_framework',
    'drf_spectacular',
    'drf_spectacular_sidecar',
    'django_filters',
    'drf_yasg',
    'corsheaders',
    'rest_framework.authtoken',



#aplicaciones (Revisar si todas son necesarias)
    'apps.api',
    'apps.auditorias',
    'apps.medidas',
    'apps.notificaciones',
    'apps.organismos',
    'apps.publico',
    'apps.reportes',
    'apps.usuarios',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.usuarios.middleware.HistorialAccesoMiddleware',
    'apps.api.middleware.APILoggingMiddleware',
    'apps.api.middleware.TokenPrefixMiddleware'
]

ROOT_URLCONF = 'ppda_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Asegúrate de que esta línea exista y apunte al directorio correcto
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

WSGI_APPLICATION = 'ppda_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Configuración para Neon (PostgreSQL) en producción
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True,
    )
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
AUTH_USER_MODEL = 'usuarios.Usuario'

REST_FRAMEWORK = {
    # Otras configuraciones de REST Framework...
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# Configuración de Spectacular
# Configuración de drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'API Plan de Descontaminación',
    'DESCRIPTION': 'API para el sistema de monitoreo del Plan de Descontaminación',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'displayOperationId': True,
        'persistAuthorization': True,
    },
    'SCHEMA_PATH_PREFIX': '/api/v1',  # Añade esta línea
    'SECURITY': [{'Bearer': []}],
    'SCHEMAS': {
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
        }
    },
    'TAGS': [  # Añade esta sección
        {'name': 'medidas', 'description': 'Endpoints relacionados con medidas'},
        {'name': 'organismos', 'description': 'Endpoints relacionados con organismos'},
        {'name': 'reportes', 'description': 'Endpoints relacionados con reportes'}
    ],
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Formato: <tu_token>'
        }
    },
}


URL_SCHEMA = '/api/schema/'


JAZZMIN_SETTINGS = {
    "site_title": "SMA Monitor",
    "site_header": "Panel Administrador Monitor SMA",
    "site_brand": "SMA",
    "site_logo": "images/logo_ppda.png",
    "theme": "slate",
    "welcome_sign": "Bienvenido al Panel de Administración del Monitor SMA",
      "topmenu_links": [
        {"name": "Inicio", "url": "/admin/", "permissions": ["auth.view_user"]},

    ],
    "icons": {
        #Probando cambiar iconos
        "auth.user": "fas fa-users",
        "usuarios.usuario": "fas fa-user-circle",
        "notificaciones.notificacion": "fas fa-bell",
        "medidas.medida": "fas fa-chart-line",
        "organismos.organismo": "fas fa-building",
        "auditorias.auditoria": "fas fa-check-circle",
        "reportes.reporte": "fas fa-file-alt",
        "organismos.contactoorganismo": "fas fa-phone-alt",
        "reportes.tiporeporte": "fas fa-clipboard-list",
        "medidas.registroavance": "fas fa-tasks",
        "usuarios.historialacceso": "fas fa-book",
        "medidas.asignacionmedida": "fas fa-ruler-combined",
        "auditorias.configuracionauditoria": "fas fa-cogs",
        "medidas.componente": "fas fa-cogs",
        "notificaciones.configuracionnotificaciones": "fas fa-bell-slash",
        "auth.group": "fas fa-users-cog",
        "reportes.visualizacion": "fas fa-eye",
        "reportes.parametroreporte": "fas fa-sliders-h",
        "notificaciones.tiponotificacion": "fas fa-bell",
        "notificaciones.recordatorio": "fas fa-clock",
        "reportes.visualizacion": "fas fa-chart-pie",
        "reportes.parametroreporte": "fas fa-sliders-h",
        "auth.group": "fas fa-users-cog",
        "organismos.tipoorganismo": "fas fa-sitemap",
        "reportes.reportegenerado": "fas fa-file-export",
        "authtoken.token": "fas fa-key",

    },


    "user_avatar": "path_to_avatar.png",

}
JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "slate",
}

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Asegúrate de que tu carpeta 'static' esté aquí
]
LOGIN_REDIRECT_URL = '/'  # Redirigir a la página principal después del login
# Configuración para los estáticos en Render
if not DEBUG:
    MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')
SITE_URL = config('SITE_URL', default='')
