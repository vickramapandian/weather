from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .models import WeatherData
from .utils import fetch_weather_from_api
from django.utils import timezone

@api_view(['GET'])
def get_weather_by_city(request, city):
    try:
        weather_data = WeatherData.objects.filter(city__iexact=city).latest('timestamp')
        return Response({
            "city": weather_data.city,
            "temperature": weather_data.temperature,
            "description": weather_data.description,
            "timestamp": weather_data.timestamp
        })
    except WeatherData.DoesNotExist:
        return Response({"error": "No data found for the specified city."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_weather_by_city(request, city):
    data = fetch_weather_from_api(city)
    if data:
        WeatherData.objects.create(
            city=data['city'],
            temperature=data['temperature'],
            description=data['description'],
            timestamp=timezone.now()
        )
        return Response({"message": f"Weather data for {city} has been updated."})
    return Response({"error": "Failed to fetch data from the API."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_weather(request):
    try:
        weather_data = WeatherData.objects.all().order_by('-timestamp')
        return Response([{
            "city": wd.city,
            "temperature": wd.temperature,
            "description": wd.description,
            "timestamp": wd.timestamp
        } for wd in weather_data])
    except WeatherData.DoesNotExist:
        return Response({"error": "No data found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_weather_by_id(request, id):
    try:
        weather_data = WeatherData.objects.get(id=id)
        weather_data.temperature = request.data.get('temperature', weather_data.temperature)
        weather_data.description = request.data.get('description', weather_data.description)
        weather_data.timestamp = timezone.now()
        weather_data.save()
        return Response({"message": f"Weather data with ID {id} has been updated."})
    except WeatherData.DoesNotExist:
        return Response({"error": "No data found for the specified ID."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_weather_by_id(request, id):
    try:
        weather_data = WeatherData.objects.get(id=id)
        weather_data.delete()
        return Response({"message": f"Weather data with ID {id} has been deleted."})
    except WeatherData.DoesNotExist:
        return Response({"error": "No data found for the specified ID."}, status=status.HTTP_404_NOT_FOUND)
    
