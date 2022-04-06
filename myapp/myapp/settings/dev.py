from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!_+t&1+uxue7vg(*s=0%ut8jix-yp_s(li_82_12wk6p)(15a&'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    
]

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")

CACHES = {
    "default" :{
        "BACKEND" : "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION" : "/home/lenovo/wagtaildoc/prcwagtail/myapp/cache"
    }
}

try:
    from .local import *
except ImportError:
    pass
