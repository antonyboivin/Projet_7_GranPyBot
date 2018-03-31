from selenium import webdriver
import unittest


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
# **User Story** He notices the page title ****and header**** mention GranPy Bot   ****** debug ******
        assert 'GrandPy Bot' in self.browser.title

# **User Story** He is invited to enter a search in a form field
# **User Story** Toto types "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
# **User Story** When he hits "enter", an icon turns to indicate that GrandPy is thinking
# **User Story** The message is displayed in the box above which displays all the messages exchanged.
# **User Story** Below, a Google Maps also appears with a marker indicating the requested address.
# **User Story** GrandPy sends a new message: ""Mais t'ai-je déjà raconté l'histoire de..."


if __name__ == '__main__':
    unittest.main(warnings='ignore')
