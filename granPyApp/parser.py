"""
    Module Docstring
"""
import json


class Parser:
    """
        The X method retrieves the request from the user.
    """
    def __init__(self, user_request):
        self.user_request = user_request

    def clean_user_request(self):
        """
            Analyze the user's request to keep only useful words.
        """

        self.user_request = self.user_request.lower()
        self.user_request = self.user_request.split(" ")

        with open("granPyApp/gpb_stopwords.json") as stop_words_file:#"granPyApp/gpb_stopwords.json"
            gpb_stopwords = json.load(stop_words_file)
        for word in gpb_stopwords:
            if word in self.user_request:
                self.user_request.remove(word)
        return self.user_request # ['openclassrooms', 'paris']


"""
testclass = "connais tu OpenClassrooms à Paris ?"


def clean_user_request(user_request):
    #Analyze the user s request to keep only useful words.

    user_request = user_request.lower()
    user_request = user_request.split(" ")

    with open("gpb_stopwords.json") as stopWordsFile:
        gpb_stopwords = json.load(stopWordsFile)
    for word in gpb_stopwords:
        if word in user_request:
            user_request.remove(word)
    print(user_request)


#clean_user_request(testclass)

testclass = "connais tu OpenClassrooms à Paris ?"
test = Parser(testclass)
print(test.clean_user_request())
"""
