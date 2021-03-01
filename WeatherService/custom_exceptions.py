
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_404_NOT_FOUND


class InvalidPlace(APIException):
    """This exception is raised when the client provides a bad city, country or 
    a bad combination of them.
    """

    status_code = HTTP_404_NOT_FOUND
    default_detail = "Place not found or not valid. Please verify that the given city and country exists and the city belongs to the country, then try again."
    default_code = "not_valid_place"