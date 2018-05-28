"""
    Script containing the functional tests of the application.
"""

import unittest
from selenium import webdriver
from granPyApp import views
from granPyApp import parser
from granPyApp import apigooglemap
from granPyApp import grandpysoul


class NewVisitorTest(unittest.TestCase):
    """
        Tests are organised into classes, which inherit from unittest.TesCase
    """
    def setUp(self):
        """
        setUp is a special method that get run before each test.
        I'm using it to start the browser.
        """
        self.browser = webdriver.Firefox()
        # creates a test client
        self.app = views.app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        """
        tearDown is a special method that get run after each test.
        I'm using it to stop the browser.
        """
        self.browser.quit()


# **User Story** Toto has heard about a cool new online search app.
# **User Story** He goes to check out its homepage
    def test_can_start_a_search_whith_GranPy_Bot(self):
        """
            Any method whose name starts with test_ is a test method,
            and will be run by the test runner.
        """
        self.browser.get('http://localhost:5000')
# **User Story** He notices the page title mention GranPy Bot
        assert 'GrandPy Bot' in self.browser.title


# **User Story** He is inveted to enter a search in a form field
    def test_user_can_make_a_request(self):
        """
            Test that the status code of the request is 200.
        """
        with self.app as client:
            sent = {'userRequest': 'Salut GrandPy ! \
                    Est ce que tu connais l adresse d OpenClassrooms ?'}
            result = client.post('/userRequest', data=sent)
        self.assertEqual(result.status_code, 200)


# **User Story** Toto types "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    def test_the_parsing_of_the_user_request(self):
        """
            Test that the Parser module handles the request
            to return only the keywords.
        """
        self.user_request = parser.Parser("Salut GrandPy ! Est ce que tu connais l adresse d OpenClassrooms ?")
# **User Story** When he click "S'il te plaît GrandPy",
    # an icon turns to indicate that GrandPy is thinking
        assert self.user_request.clean_user_request() == ['openclassrooms']


# **User Story** The message is displayed in the box above
    # which displays all the messages exchanged.
    def test_the_localisation_of_the_user_request(self):
        """
        Test that the Google map method return
        the latitude and the longitude data.
        """
        self.user_request = apigooglemap.GoogleMapsApi(['openclassrooms'])
# **User Story** Below, a Google Maps also appears with a marker indicating the requested address.
        assert self.user_request.googlemaps_apicall()[0] == {'lat': 48.8747578,
                                                             'lng': 2.350564700000001}


# **User Story** GrandPy sends a new message: "Mais t'ai-je déjà raconté l'histoire de..."
    def test_GrandPy_send_a_second_message_with_a_story(self):
        """
            Test that GrandPy-Bot returned a response in 2 steps.
        """
        self.grandpy_soul = grandpysoul.GrandPySoul()
        assert self.grandpy_soul.formatted_address_quote() == "Biensur mon poussin, l'adresse est "


if __name__ == '__main__':
    unittest.main(warnings='ignore')
