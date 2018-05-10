"""
    This module will manage the Wikipedia API call
    to return useful values ​​for the application.
"""
import requests


class WikipediaApi:
    """
        This Class includes all the parameters necessary to call the API
        in order to process the response and return the useful values.
    """
    def __init__(self, user_request):
        self.url = 'https://fr.wikipedia.org/w/api.php?'
        self.user_request = user_request
        self.parametres = {'action' : 'opensearch',
                           'search' : self.user_request,
                           'limit' :1}
        self.api_request = requests.get(self.url, params=self.parametres)
        self.api_response = self.api_request.json()


    
    def wikipedia_apicall(self):
        """
            Returns a description of the user request.
        """
        # print(self.api_request.url)
        # print(self.api_response[2])
        return self.api_response[2]
