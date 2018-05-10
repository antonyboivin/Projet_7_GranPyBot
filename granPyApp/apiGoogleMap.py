"""
    This module will manage the Google Maps API call
    to return useful values ​​for the application.
"""
import requests


class GoogleMapsApi:
    """
        This Class includes all the parameters necessary to call the API
        in order to process the response and return the useful values.
    """
    def __init__(self, user_request):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.user_request = user_request
        self.key = ['AIzaSyBJoClBGNF-tJf3Gq1QY6v1zK6O09_2nrg']
        self.parametres = {'address' : self.user_request, 'key' : self.key}
        self.api_request = requests.get(self.url, params=self.parametres)
        self.api_response = self.api_request.json()['results'][0]['geometry']['location']


    def googlemaps_apicall(self):
        """
            Returns the value as: "{'lat': 48.8747578, 'lng': 2.350564700000001}".
        """
        return self.api_response
