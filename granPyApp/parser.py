"""
    This module will analyze the user's request and
    then return the useful values ​​to the application.
"""
import json


class Parser:
    """
        This Class will take into account the user's request in order
        to apply the class method necessary for its analysis.
    """
    def __init__(self, user_request):
        self.user_request = user_request

    def clean_user_request(self):
        """
            Analyze the user's request to keep only useful words.
            Example of a user request:"Connais tu Openclassrooms à Paris ?"
            Returns the value: "['openclassrooms', 'paris']"
        """
        self.user_request = self.user_request.lower()
        self.user_request = self.user_request.split(" ")

        with open("granPyApp/gpb_stopwords.json") as stop_words_file:
            gpb_stopwords = json.load(stop_words_file)
        for word in gpb_stopwords:
            if word in self.user_request:
                self.user_request.remove(word)
        return self.user_request
