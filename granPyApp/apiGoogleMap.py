import requests


import requests


class GoogleMapsApi:
    def __init__(self, userRequest):
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json'
        self.userRequest = userRequest
        self.key = ['AIzaSyBJoClBGNF-tJf3Gq1QY6v1zK6O09_2nrg']
        self.parametres = {'address' : self.userRequest, 'key' : self.key }


    def GoogleMapsApiCall(self):
        self.apiRequest = requests.get(self.url, params=self.parametres)
        self.apiResponse = self.apiRequest.json()['results'][0]['geometry']['location']
        return self.apiResponse # {'lat': 48.8747578, 'lng': 2.350564700000001}

