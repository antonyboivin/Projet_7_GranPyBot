"""
    Script containing the functional tests of the application.
"""


import urllib.request
import json
from io import BytesIO
from granPyApp import apigooglemap
from granPyApp import apiwikipedia


class TestMockApi:
    """
        The tests are organized in classes, which contain the API test methods.
    """
    def test_googlemap_api_http_return(self, monkeypatch):
        results = {
            "results" : [
                {
                    "formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                    "geometry" : {
                        "location" : {
                            "lat" : 48.8747578,
                            "lng" : 2.350564700000001
                            },
                        },
                    }
                ],
            "status" : "OK"
            }

        def mockreturn(request):
            return results

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        maps = apigooglemap.GoogleMapsApi(['openclassrooms'])
        assert maps.googlemaps_apicall()[0] == results['results'][0]['geometry']['location']

    def test_wikipedia_api_http_return(self, monkeypatch):
        results = ["openclassrooms", ["OpenClassrooms"],
                   ["OpenClassrooms est une \u00e9cole en ligne. Chaque visiteur peut \u00e0 la fois \u00eatre un lecteur ou un r\u00e9dacteur."],
                   ["https://fr.wikipedia.org/wiki/OpenClassrooms"]]

        def mockreturn(request):
            return results

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        wiki = apiwikipedia.WikipediaApi(['openclassrooms'])
        assert wiki.wikipedia_apicall()[0] == results[2]
