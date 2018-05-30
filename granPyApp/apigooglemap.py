"""
    This module will manage the Google Maps API call
    to return useful values ​​for the application.
"""
import requests
import config
from .grandpysoul import GrandPySoul


class GoogleMapsApi:
    """
        This Class includes all the parameters necessary to call the API
        in order to process the response and return the useful values.
    """
    def __init__(self, user_request):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.user_request = user_request
        self.key = config.GOOGLE_MAP_KEY
        self.parametres = {'address' : self.user_request, 'key' : self.key}
        # Definition of the URL
        self.api_request = requests.get(self.url, params=self.parametres)
        # Création of a GrandPySpul object
        self.grandpy_soul = GrandPySoul()


    def googlemaps_apicall(self):
        """
            Check the code status of the request and if 'ok' return :
            Returns the value as:
            "{'lat': 48.8747578, 'lng': 2.350564700000001} 7 Cité Paradis, 75010 Paris, France".
        """
        if self.api_request.json()['status'] == "OK":
            # Definition of location in terms of latitude and longitude
            self.api_response_location = self.api_request.json()['results'][0]['geometry']['location']
            # Definition of the formatted address
            self.api_response_formatted_address = self.api_request.json()['results'][0]['formatted_address']
            # GrandPySoul method call for the formatted address
            self.grandpy_soul = self.grandpy_soul.formatted_address_quote()

            return self.api_response_location, self.api_response_formatted_address, self.grandpy_soul

        else:
            # GrandPySoul method call for the error message
            self.grandpy_soul = self.grandpy_soul.error_message_quote()
            # Definition of location in terms of latitude and longitude
            self.api_response_location = {}
            # Definition of the formatted address
            self.api_response_formatted_address = ""
           
            return self.api_response_location, self.api_response_formatted_address, self.grandpy_soul
