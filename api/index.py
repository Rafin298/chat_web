import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = get_wsgi_application()

def handler(event, context):
    return app(event, context)