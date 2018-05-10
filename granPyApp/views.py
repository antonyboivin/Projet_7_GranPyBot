from flask import Flask, render_template, request, jsonify
from .parser import Parser
from .apigooglemap import GoogleMapsApi
from .apiwikipedia import WikipediaApi

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/userRequest', methods=['POST'])
def analysis():
    """
        Analysis of the user's request to extract the keywords
        and determine the geographic coordinates and a textual description.
    """
    # Creation of a Parser object with the request of the user.
    userRequest = Parser(request.form['userRequest'])
    # Returns the keywords of the user's request.
    userRequest = userRequest.clean_user_request()

    # Creation of a GoogleMapsApi object with the request of the user.
    userRequestLocation = GoogleMapsApi(userRequest)
    # Returns the coordinate of the user's request.
    userRequestLocation = userRequestLocation.googlemaps_apicall()

    # Creation of WikipediaApi object whith the userRequest.
    userRequestDescription = WikipediaApi(userRequest)
    userRequestDescription = userRequestDescription.wikipedia_apicall()

    # Grouping of geographic and text data in the "datas" variable
    datas = {"coordinate" : userRequestLocation,
             "description" : userRequestDescription}

    return jsonify(datas)


"""
 def analysis():
    userRequest = Parser(request.form['userRequest'])
    userRequest = userRequest.clean_user_request()

    userRequestLocation = GoogleMapsApi(userRequest)
    userRequestLocation = userRequestLocation.GoogleMapsApiCall()
    
    return jsonify(userRequestLocation)
"""


if __name__ == "__main__":
    app.run()
