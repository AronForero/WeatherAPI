from django.urls import path
from WeatherService.views import WeatherViewSet

weather_ops = WeatherViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path(
        'city/<str:city>/country/<str:country>',
        weather_ops,
        name='weather_operations',
    )
]
