from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-x=tu5%d@nyz&r729)#t^n9lcp(tv2g@_7ux=_vywi3 mb8rn7ol'
DEBUG = True
ALLOWED_HOSTS = []

# -----------------------------
# اپ‌ها
# -----------------------------
INSTALLED_APPS = [
    'format_hub',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# -----------------------------
# Middleware
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # فولدر عمومی برای تمپلیت
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

WSGI_APPLICATION = 'setting.wsgi.application'

# -----------------------------
# دیتابیس
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# زبان و زمان
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# استاتیک
# -----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # فولدر عمومی برای استاتیک
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # برای collectstatic در پروداکشن

# -----------------------------
# مدیا
# -----------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # فایل‌های آپلود شده اینجا ذخیره میشن

# -----------------------------
# برای فایل‌های بزرگ یا مسیرهای خاص
# -----------------------------
# اگه نیاز باشه می‌تونی حداکثر سایز آپلود و زمان آپلود رو هم محدود کنی
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10MB

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
