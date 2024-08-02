from celery import shared_task
from .models import WeatherData
from .utils import fetch_weather_from_api
from django.utils import timezone

@shared_task
def fetch_weather_data():
    cities = ['London', 'New York']
    for city in cities:
        data = fetch_weather_from_api(city)
        if data:
            WeatherData.objects.create(
                city=data['city'],
                temperature=data['temperature'],
                description=data['description'],
                timestamp=timezone.now()
            )
