from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
app = Celery('your_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'receiving_actual_currency_rates_every_24_hours': {
        'task': 'app.tasks.get_currency_rates_dict_task',
        'schedule': crontab(hour='11', minute='11'),
    },
}