"""
WSGI config for Bigflow project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/bigb/Bigflow')
sys.path.append('/var/www/bigb/venv/lib/python3.5/site-packages')

os.environ["DJANGO_SETTINGS_MODULE"]= "Bigflow.settings"
#os.environ['HTTPS']="ON"
#from django.core.wsgi import get_wsgi_application

try:
	application = get_wsgi_application()
	#application = DjangoWhiteNoise(application)
except Exception:
	if 'mod_wsgi' in sys.modules:
		traceback.print_exc()
		os.kill(os.getpid(),signal.SIGINT)
		time.sleep(2)
