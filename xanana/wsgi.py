"""
WSGI config for xanana project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from __future__ import absolute_import, unicode_literals

import os

from django.core.wsgi import get_wsgi_application
import dotenv

# Load up environment variables from the closest `.env` file
dotenv.load_dotenv(dotenv.find_dotenv())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xanana.settings.dev")

application = get_wsgi_application()
