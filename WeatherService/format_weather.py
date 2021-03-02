import json
from datetime import datetime

def format_wind_direction(wind_degrees):
    """Recieves a number (degrees) and transform it to a readable
    direction

    Args:
        wind_degrees ([int]): direction of the wind in degrees

    Returns:
        [str]: human readable direction
    """
    wind_directions = {
        "N": "North",
        "NNE": "North-NorthEast",
        "NE": "NorthEast",
        "ENE": "East-NorthEast",
        "E": "East",
        "ESE": "East-SouthEast",
        "SE": "SouthEast",
        "SSE": "South-SouthEast",
        "S": "South",
        "SSW": "South-SouthWest",
        "SW": "SouthWest",
        "WSW": "West-SouthWest",
        "W": "West",
        "WNW": "West-NorthWest",
        "NW": "NorthWest",
        "NNW": "North-NorthWest",
    }
    idx_wind_dir = 0 if round((wind_degrees%360)/22.5) == 16 else round((wind_degrees%360)/22.5)
    abbr_wind_dir = list(wind_directions.keys())[idx_wind_dir]
    wind_dir = wind_directions[abbr_wind_dir]

    return wind_dir

def beaufort_scale_format(wind_speed):
    """Receives the speed of the wind, and transform it to a 
    human readable format based on beaufort scale

    Args:
        wind_speed ([float]): wind speed in m/s

    Returns:
        [str]: Name of the wind speed based on Beafort's Scale
    """
    beaufort_scale = {
        0.5: 'Calm',
        1.5: 'Light-air',
        3.3: 'Light Breeze',
        5.5: 'Gentle Breeze',
        7.9: 'Moderate Breeze',
        10.7: 'Fresh Breeze',
        13.8: 'Strong Breeze',
        17.1: 'High Wind',
        20.7: 'Fresh Gale',
        24.4: 'Strong/Severe Gale',
        28.4: 'Storm',
        32.6: 'Violent Storm',
        99999999: 'Hurricane'
    }
    for speed in beaufort_scale:
        if wind_speed < speed:
            beaufort_wind_speed = beaufort_scale[speed]
            break
    return beaufort_wind_speed

def format_weather(api_response):
    """This function receives the data returned by the weather API, and formats
    it leaving just the necessary data that would be returned to the client.

    Args:
        api_response ([dictionary]): contains the data returned by the external
        API.
    returns:
        response_dict [dictionary]: the expected structure by the client.
    """
    weather_data_dict = json.loads(api_response.content)

    # Wind Direction format
    wind_dir = format_wind_direction(weather_data_dict.get('wind').get('deg'))

    # Wind Beaufort scale format
    beaufort_wind_speed = beaufort_scale_format(weather_data_dict.get('wind').get('speed'))

    response_dict = {
            'location_name': weather_data_dict.get('name')+','+weather_data_dict.get('sys').get('country'),
            'temperature': str(weather_data_dict.get('main').get('temp')-273.15)+' °C',
            'wind': beaufort_wind_speed+', '+str(weather_data_dict.get('wind').get('speed'))+' m/s, '+wind_dir,
            'cloudiness': weather_data_dict.get('weather')[0].get('description'),
            'pressure': str(weather_data_dict.get('main').get('pressure'))+' hpa',
            'humidity': str(weather_data_dict.get('main').get('humidity'))+'%',
            'sunrise': datetime.fromtimestamp(weather_data_dict.get('sys').get('sunrise'))\
                .strftime("%I:%M"),
            'sunset': datetime.fromtimestamp(weather_data_dict.get('sys').get('sunset'))\
                .strftime("%I:%M"),
            'geo_coordinates': [weather_data_dict.get('coord').get('lat'),\
                 weather_data_dict.get('coord').get('lon')],
            'requested_time':datetime.fromtimestamp(
                                weather_data_dict.get('dt')
                            ).strftime("%Y-%m-%d %I:%M:%S"),
            'forecast': {},
        }
    return response_dict
