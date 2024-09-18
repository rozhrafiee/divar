import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_divar.settings')

app = Celery('my_divar')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()