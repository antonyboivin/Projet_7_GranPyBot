"""
    This module will manage the Google Maps API call
    to return useful values ​​for the application.
"""
import requests
import config


class GoogleMapsApi:
    """
        This Class includes all the parameters necessary to call the API
        in order to process the response and return the useful values.
    """
    def __init__(self, user_request):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.user_request = user_request
        self.key = config.GOOGLE_MAP_KEY #['AIzaSyBJoClBGNF-tJf3Gq1QY6v1zK6O09_2nrg']
        self.parametres = {'address' : self.user_request, 'key' : self.key}
        self.api_request = requests.get(self.url, params=self.parametres)
        self.api_response = self.api_request.json()['results'][0]['geometry']['location']
        #self.api_response_deux = self.api_request.json()['status']
        # self.api_response['results'][0]['formatted_address'] retourne l'adresse postale ex : 7 Cité Paradis, 75010 Paris, France (pour openclassrooms)

    def googlemaps_apicall(self):
        """
            Returns the value as: "{'lat': 48.8747578, 'lng': 2.350564700000001}".
        """
        return self.api_response
    """
        if self.api_response_deux['status'] == "OK":
            print(self.api_response)
            return self.api_response
        else:
            print("pas de réponse !")
    """