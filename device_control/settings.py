from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-#k7&x%zy7ck^v$3)jtevf8k(r1%b*op-$sgf(^50gh*st=taq7'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom Middlewares
    'device_control.middlewares.TemplateRenderer',
]

ROOT_URLCONF = 'device_control.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'device_control.context_processors.custom_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'device_control.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom Settings
LOGIN_URL = '/login'
AUTH_USER_MODEL = "users.UserLogin"
URL_PAGES = [
    {
        "href" : "/",
        "name" : "Dashboard",
        "is_menu" : True,
        "template" : "index.html",
        "login_required" : True,
        "classes": "fas fa-tachometer-alt me-3"
    },
    {
        "href" : "/login",
        "name" : "Login to Device Control",
        "is_menu" : False,
        "template" : "login.html",
        "login_required" : False,
    },
    {
        "href" : "/register",
        "name" : "Regiter in Device Control",
        "is_menu" : False,
        "template" : "register.html",
        "login_required" : False,
    },
    {
        "href" : "/devices",
        "name" : "Devices",
        "is_menu" : True,
        "template" : "devices.html",
        "login_required" : True,
        "classes" : "fas fa-mobile-alt me-3",
    },
    {
        "href" : "/devices-details",
        "name" : "Devices Details",
        "is_menu" : False,
        "template" : "devices-details.html",
        "login_required" : True,
        "classes" : "fas fa-mobile-alt me-3",
    },
    {
        "href" : "/cmd-center",
        "name" : "Command Center",
        "is_menu" : True,
        "template" : "commands.html",
        "login_required" : True,
        "classes" : "fas fa-terminal me-3",
    },
    {
        "href" : "/admin-settings",
        "name" : "Admin / Settings",
        "is_menu" : True,
        "template" : "admin-page.html",
        "login_required" : True,
        "classes" : "fas fa-gear me-3",
    },
    {
        "href" : "/logout",
        "name" : "Logout",
        "is_menu" : True,
        "template" : "N/A",
        "login_required" : True,
        "classes" : "fas fa-sign-out-alt me-3",
    },
]