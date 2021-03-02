from django.test import TestCase

from rest_framework.test import APITransactionTestCase
from WeatherService.test.mock_server import start_mock_server


class GETWeather(APITransactionTestCase):
    """Tests Class, contains the functional tests for the application.

    NOTE: This tests should run using the mock server, but for the sake of this
    technical task, the tests will run against the external server, even if
    it is a bad practice.
    """
    reset_sequences = True

    def setUp(self):
        start_mock_server(8124)

    def test_1_uncomplete_kwargs(self):
        """Simulates what happen if the keyword arguments are not passed
        """
        request = self.client.get(
            '/weather/city/Bucaramanga/country/',
        )
        assert (request.status_code == 404)

    def test_2_invalid_place(self):
        """Show he behaviour of the endpoint when an invalid country or city are
        passed
        """
        request1 = self.client.get(
            '/weather/city/medellin/country/hk',
        )

        request2 = self.client.get(
            '/weather/city/x32/country/co',
        )

        assert (request1.status_code == request2.status_code == 404)
        assert (request1.data['detail'] == \
            request2.data['detail'] == \
            'Place not found or not valid. Please verify that the given city and country exists and the city belongs to the country, then try again.'
        )

    def test_3_correct_weather_request(self):
        """What should be the behaviour of the endpoint.
        """
        request = self.client.get(
            '/weather/city/Bucaramanga/country/co',
        )
        expected_response = {
            "location_name": "Bucaramanga,CO",
            "temperature": "23.0 °C",
            "wind": "Light Breeze, 2.57 m/s, NorthWest",
            "cloudiness": "scattered clouds",
            "pressure": "1011 hpa",
            "humidity": "68%",
            "sunrise": "11:05",
            "sunset": "11:04",
            "geo_coordinates": [
                7.1254,
                -73.1198
            ],
            "requested_time": "2021-03-02 12:13:07",
            "forecast": {}
        }
        assert (request.status_code == 200)
        for key in expected_response.keys():
            assert (key in request.data)
