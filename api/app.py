from . import app
from .src import temperature_conversion
from .resources import temperature

if __name__ == '__main__':
    app.run(debug=True)
