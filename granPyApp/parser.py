import json


class Parser:
    def __init__(self, user_request):
        self.user_request = user_request

    def clean_user_request(self):
        """
            Analyze the user's request to keep only useful words.
        """

        self.user_request = self.user_request.lower()
        self.user_request = self.user_request.split(" ")

        with open("granPyApp/gpb_stopwords.json") as stopWordsFile:
            gpb_stopwords = json.load(stopWordsFile)
        for word in gpb_stopwords:
            if word in self.user_request:
                self.user_request.remove(word)
        return self.user_request
        

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

testclass = "connais tu OpenClassrooms à Paris ?"
#clean_user_request(testclass)
test = Parser(testclass)
print(test.clean_user_request())
"""




