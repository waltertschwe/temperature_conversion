from functools import wraps

class TemperatureConversion():
    """ Convert different types of temperature """

    def __init__(self):
        """ initialize class """
        self.kelvin_freezing = 273.15
        self.rankine_freezing = 491.67
        self.fahrenheit_freezing = 32

    def is_input_number(conversion_func):
        """ decorator function to check if input is an integer or float """
        @wraps(conversion_func)
        def wrapper_check_number(*args, **kwargs):
            try:
                if not isinstance(args[1], (int, float)):
                    return None
            except:
                return None
            return conversion_func(*args, **kwargs)
        return wrapper_check_number

    @is_input_number
    def kelvin_to_celsius(self, kelvin):
        """ convert a kelvin temperature to celsius """
        return round((kelvin - self.kelvin_freezing), 2)

    @is_input_number
    def kelvin_to_fahrenheit(self, kelvin):
        """ convert a kelvin temperate to fahrenheit """
        return round((kelvin - self.kelvin_freezing) * 9/5 + self.fahrenheit_freezing, 2)

    @is_input_number
    def kelvin_to_rankine(self, kelvin):
        """ convert a kelvin temperature to rankine """
        return round((kelvin * 1.8), 2)

    @is_input_number
    def celsius_to_kelvin(self, celsius):
        """ convert celsius temperature to kelvin """
        return round((celsius + self.kelvin_freezing), 2)

    @is_input_number
    def celsius_to_fahrenheit(self, celsius):
        """ convert celsius temperature to fahrenheit """
        return round((celsius * 9/5) + self.fahrenheit_freezing, 2)

    @is_input_number
    def celsius_to_rankine(self, celsius):
        """ convert celsius temperature to rankine """
        return round((celsius * 9/5) + self.rankine_freezing, 2)

    @is_input_number
    def fahrenheit_to_kelvin(self, fahrenheit):
        """ convert fahrenheit temperature to kelvin """
        return round((fahrenheit - self.fahrenheit_freezing) * 5/9 + self.kelvin_freezing, 2)

    @is_input_number
    def fahrenheit_to_celsius(self, fahrenheit):
        """ convert fahrenheit temperature to celsius """
        return round((fahrenheit - self.fahrenheit_freezing) * 5/9, 2)

    @is_input_number
    def fahrenheit_to_rankine(self, fahrenheit):
        """ convert fahrenheit temperature to rankine """
        return round((fahrenheit + 459.67), 2)

    @is_input_number
    def rankine_to_kelvin(self, rankine):
        """ convert rankine temperature to kelvin """
        return round((rankine * 5/9), 2)

    @is_input_number
    def rankine_to_celsius(self, rankine):
        """ convert rankine temperature to celsius """
        return round((rankine - self.rankine_freezing) * 5/9, 2)

    @is_input_number
    def rankine_to_fahrenheit(self, rankine):
        """ convert rankine to fahrenheit """
        return round((rankine - 459.67), 2)
