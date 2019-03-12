Temperature Conversion API

=== Pre-Installation ===

python3
virutalenv
pip

=== Installation ===
```bash
git clone git@github.com:waltertschwe/temperature_conversion.git

cd temperature_conversion

virtualenv -p python3 api/

source api/bin/activate

pip install -r requirements.txt

export FLASK_APP=$fullPathToApp/app.py

flask run
```
