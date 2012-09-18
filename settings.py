# Django settings for nizapp project.
import django.contrib.auth
import os.path





DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
          ('bhjo','gninyx@gmail.com'),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'mobile',                      # Or path to database file if using sqlite3.
        'USER': 'evens',                      # Not used with sqlite3.
        'PASSWORD': 'evens1025',                  # Not used with sqlite3.
        #'ENGINE': 'django.db.backends.sqlite3', 
        #'NAME': '/var/www/django/nizapp/sqlite.db',                      # Or path to database file if using sqlite3.
        #'USER': '',                      # Not used with sqlite3.
        #'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
DATABASE_OPTIONS = {'charset': 'utf8'}
TIME_ZONE = 'Asia/Seoul'
LANGUAGE_CODE = 'ko-kr'



DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET='utf-8'
FILE_CHARSET='utf-8'
USE_I18N = True
USE_L10N = True


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'utf-8'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/evens/www/mobile/nizapp/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'
STATIC_URL ='/app/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'oy&vb733tkjj(0d02ubxcw@#k2^d8_(gks&gfq8!bckpvv_i-i'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

)

ROOT_URLCONF = 'nizapp.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'nizapp.niz',
    'django.contrib.comments',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)


LOGIN_URL = '/login/'

#bit.ly 
#BITLY_ID="ninyx"
#BITLY_PW="gandy22"
#BITLY_API="R_56b1cd85f02981b70393f425fd3c747f"

BITLY_ID="nizus"
BITLY_PW="abcd1234"
BITLY_API="R_3ad0d80e011e2608a97ca0429e954f9c"


#image upload
#UPLOAD_TO = 'niz/upload/thumbnails/'
UPLOAD_TO = 'nizapp/upload/'

