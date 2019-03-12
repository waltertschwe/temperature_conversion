from flasgger.utils import swag_from
from flask import request

from .. import app
from ..src.temperature_conversion import TemperatureConversion as tc

@app.route('/temperature', methods = ['POST'])
@swag_from('../docs/temperature_conversion.yml')
def temperature_conversion():
    """ Temperature Conversion POST """

    ## get post parameters
    conversion_type = request.data.get('conversion_type')
    input_temp = request.data.get('input_temp')
    student_response = request.data.get('student_response')

    ## use tc class to call correct function to do the conversion
    tc_obj = tc()
    function_to_call = getattr(tc_obj, conversion_type)
    conversion_result = function_to_call(input_temp)

    ## return the response
    data = {}
    response = {}
    if conversion_result:
        ## process a converion was a success
        data['conversion_result'] = conversion_result
        if conversion_result == student_response:
            data['is_correct'] = True
        else:
            data['is_correct'] = False
    else:
        ## could not process conversion based on inputs
        data['error'] = True

    response['result'] = data

    return response
