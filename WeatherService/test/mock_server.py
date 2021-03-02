# Standard library imports...
import json
import re
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

# Third-party imports...
import requests


class MockServerRequestHandler(BaseHTTPRequestHandler):

    INVALID_GIVEN_PLACES_1 = re.compile(r'Bucaramanga,hk&appid=SECRETSECRETSECRET')
    INVALID_GIVEN_PLACES_2 = re.compile(r'x32,co&appid=SECRETSECRETSECRET')
    CORRECT_URL = re.compile(r'Bucaramanga,co&appid=SECRETSECRETSECRET')

    def do_GET(self):

        if re.search(self.INVALID_GIVEN_PLACES_1, self.path):
            # Add response status code.
            self.send_response(requests.codes.not_found)

            # Add response headers.
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()

            # Add response content.
            response_content = json.dumps(
                {
                "cod": "404",
                "message": "city not found"
                }
            )
            self.wfile.write(response_content.encode('utf-8'))
            return

        if re.search(self.INVALID_GIVEN_PLACES_2, self.path):
            # Add response status code.
            self.send_response(requests.codes.not_found)

            # Add response headers.
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()

            # Add response content.
            response_content = json.dumps(
                {
                "cod": "404",
                "message": "city not found"
                }
            )
            self.wfile.write(response_content.encode('utf-8'))
            return

        if re.search(self.CORRECT_URL, self.path):
            # response code.
            self.send_response(requests.codes.ok)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            
            # Add response content.
            response_content = json.dumps(
                {
                    "coord": {
                        "lon": -73.1198,
                        "lat": 7.1254
                    },
                    "weather": [
                        {
                        "id": 802,
                        "main": "Clouds",
                        "description": "scattered clouds",
                        "icon": "03n"
                        }
                    ],
                    "base": "stations",
                    "main": {
                        "temp": 296.15,
                        "feels_like": 296.64,
                        "temp_min": 296.15,
                        "temp_max": 296.15,
                        "pressure": 1011,
                        "humidity": 68
                    },
                    "visibility": 10000,
                    "wind": {
                        "speed": 2.57,
                        "deg": 310
                    },
                    "clouds": {
                        "all": 40
                    },
                    "dt": 1614646078,
                    "sys": {
                        "type": 1,
                        "id": 8581,
                        "country": "CO",
                        "sunrise": 1614596718,
                        "sunset": 1614639875
                    },
                    "timezone": -18000,
                    "id": 3688465,
                    "name": "Bucaramanga",
                    "cod": 200
                }
            )
            self.wfile.write(response_content.encode('utf-8'))
            return

def start_mock_server(port):
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    result = s.connect_ex(('localhost', port))
    if result != 0:
        mock_server = HTTPServer(('localhost', port), MockServerRequestHandler)
        mock_server_thread = Thread(target=mock_server.serve_forever)
        mock_server_thread.setDaemon(True)
        mock_server_thread.start()
