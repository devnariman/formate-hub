from pathlib import Path
import os

# مسیر پایه پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# امنیت و دیباگ
SECRET_KEY = 'django-insecure-dvafx53q(23sgm9wp7(fgsf=nmwc0c2@e_--m_&nd(r-6po0_1'
DEBUG = True
ALLOWED_HOSTS = []

# اپلیکیشن‌ها
INSTALLED_APPS = [
    'main',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL و WSGI
ROOT_URLCONF = 'format_hub.urls'
WSGI_APPLICATION = 'format_hub.wsgi.application'

# دیتابیس
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# قالب‌ها (Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # پوشه templates خارج از اپ
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# پسورد والیدیشن
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# بین‌المللی‌سازی
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# فایل‌های استاتیک
STATIC_URL = '/static/'

# مسیر اضافی فایل‌های استاتیک (فولدر static کنار manage.py)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# کلید پیش‌فرض برای مدل‌ها
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
