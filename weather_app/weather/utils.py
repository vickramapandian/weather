import requests
from django.conf import settings

def fetch_weather_from_api(city):
    try:
        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'timestamp': data['dt']
            }
        else:
            return None
    except Exception as e:
        return (f"An error occurred: {str(e), response.status_code}")