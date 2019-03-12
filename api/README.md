**"Remember, a few hours of trial and error can save you several minutes of looking at the README."**

Temperature Conversion API

```bash
git clone git@github.com:waltertschwe/temperature_conversion.git

cd temperature_conversion

virtualenv -p python3 api/

source api/bin/activate

pip install -r requirements.txt

export FLASK_APP=$fullPathToApp/app.py

flask run
```
