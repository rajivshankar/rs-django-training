"""
WSGI config for exercises project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

#commented due to Heroku
#import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

#commented due to Heroku
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exercises.settings")

#commented due to Heroku
#application = get_wsgi_application()

application = Cling(get_wsgi_application())