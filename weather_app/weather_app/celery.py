from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('weather_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Periodic Task schedule
from celery.schedules import crontab
app.conf.beat_schedule = {
    'fetch-weather-every-hour': {
        'task': 'weather.tasks.fetch_weather_data',
        'schedule': crontab(minute=0, hour='*/1'),  # Every hour
    },
}
