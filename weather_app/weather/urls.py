from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/', views.get_weather_by_city, name='get_weather_by_city'),
    path('weather/', views.get_all_weather, name='get_all_weather'),
    path('weather/update/<str:city>/', views.update_weather_by_city, name='update_weather_by_city'),
    path('weather/<int:id>/', views.update_weather_by_id, name='update_weather_by_id'),
    path('weather/<int:id>/', views.delete_weather_by_id, name='delete_weather_by_id'),
]
