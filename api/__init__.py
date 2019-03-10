from flask import request
from flask_cors import CORS
from flask_api import FlaskAPI
from flasgger import Swagger

app = FlaskAPI(__name__)
app.config['SWAGGER'] = {
    'title': 'Temperature Conversion',
}

template = {
  "swagger": "2.0",
  "info": {
    "title": "Temperature Conversion App",
    "description": "Temperature Conversion for Fahrenheit, Celsius, Kelvin and Rankine",
    "contact": {
      "responsibleOrganization": "Technology",
      "responsibleDeveloper": "Walter Schweitzer",
      "email": "wschweitzer00@gmail.com",
      "url": "http://github.com/waltertschwe",
    },
    "termsOfService": "None",
    "version": "1.0.0"
  },
  "schemes": [
    "http",
    "https"
  ],
}

Swagger(app, template=template)
CORS(app)
