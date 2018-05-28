# GrandPy Bot, le papy-robot

"GrandPy Bot, le papy-robot" is an application written in python via the Flask module as part of Openclassrooms' "Application Developer - Python" training.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

Download and install python 3.5.6.

### Installing

A step by step series of examples that tell you have to get a development env running.


```
$ pip install -r requirements.txt
```

Activate your virtual environnement

```
cd VENV
scripts\activate
```

Back to main folder "grandPyApp" and start the server

```
python run.py
```

Now you can access the web application by entering http://127.0.0.1:5000 in the address bar of your favorite browser.

## Running the tests

You can run tests by running the files:

```
python test_functional.py
python test_mockapi.py
```

### Break down into end to end tests

Tests are organised into classes, which inherit from unittest.TesCase
Exemple:
```
def test_can_start_a_search_whith_GranPy_Bot(self):
    self.browser.get('http://localhost:5000')
    assert 'GrandPy Bot' in self.browser.title
```

## Deployment

The app is deployed on Heroku at

## Built With

* [Heroku](https://www.heroku.com/) - The Cloud Application Platform.
* [Python](https://www.python.org/) - The base.
* [Openclassrooms](https://openclassrooms.com/) - Graduate courses and free courses...

## Authors

* **Antony BOIVIN** - *Initial work* - [antonyboivin](https://github.com/antonyboivin)

