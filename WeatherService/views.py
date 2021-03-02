"""This Module containes the Views of the service.

Exports:
    home: basic endpoint that returns a 'Hello World'
    WeatherViewSet: contains the endpoint that provides the weather given a city
    and a country code.
"""

import os

import requests
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from WeatherService.custom_exceptions import InvalidPlace
from WeatherService.format_weather import format_weather


@api_view(['GET'])
@permission_classes((AllowAny, ))
def home(request):
    return JsonResponse(
        {"Hello": "World"},
        status=status.HTTP_200_OK,
    )


class WeatherViewSet(viewsets.ViewSet):
    """
    Allows the users to get the weather
    """
    @method_decorator(cache_page(60*2))
    def retrieve(self, request, *args, **kwargs):
        """Recieves the GET requests, returning the weather of the specified city
        """

        # NOTE: If you want to run the application with environment variables,
        # please uncomment the following lines of code. and comment the next 3
        # lines of code (lines 51, 52, and 53).
        # the app id is brought with an env variable.
        # weather_url = os.getenv('WEATHER_URL')+\
        #     kwargs.get('city')+','+kwargs.get('country')+\
        #     '&appid='+os.getenv('OWM_APPID')
            # '&appid=1508a9a4840a5574c822d70ca2132032'

        weather_url = 'http://api.openweathermap.org/data/2.5/weather?q='+\
            kwargs.get('city')+','+kwargs.get('country')+\
            '&appid=1508a9a4840a5574c822d70ca2132032'
        
        weather_response = requests.get(weather_url)
        if weather_response.status_code == 404:
            raise InvalidPlace

        response_dict = format_weather(weather_response)

        return Response(
            response_dict,
            status=status.HTTP_200_OK,
            content_type='application/json')
