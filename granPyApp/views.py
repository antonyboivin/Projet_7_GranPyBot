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
    # Returns the description of the user's request.
    userRequestDescription = userRequestDescription.wikipedia_apicall()


    # Grouping of geographic and text data in the "datas" variable
    datas = {"coordinate" : userRequestLocation[0],
             "formatted_address" : userRequestLocation[1],
             "grandPy_formatted_address" : userRequestLocation[2],
             "description" : userRequestDescription[0],
             "grandPy_description" : userRequestDescription[1]}

    return jsonify(datas)




#if __name__ == "__main__":
#    app.run()
