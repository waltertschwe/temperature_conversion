from flasgger.utils import swag_from
from flask import request

from .. import app
from ..src.temperature_conversion import TemperatureConversion as tc

@app.route('/temperature', methods = ['POST'])
@swag_from('../docs/temperature_conversion.yml')
def temperature_conversion():
    """ Temperature Conversion """

    #conversion_type = request.data.get('conversion_type')
    #input_temp = request.data.get('input_temp')
    #student_response = request.data.get('student_response')

    tc_obj = tc()
    input_temp = 34.7
    result = tc_obj.kelvin_to_celsius(input_temp)
    data = {}
    data['result'] = result

    return data
