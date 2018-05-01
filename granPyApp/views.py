from flask import Flask, render_template, request, jsonify
from .parser import Parser


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/userRequest', methods=['POST'])
def analysis():
    userRequest = Parser(request.form['userRequest'])
    userRequest = userRequest.clean_user_request()
    return jsonify(userRequest)


if __name__ == "__main__":
    app.run()
