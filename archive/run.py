#!venv/bin/python
import os
# TODO: recreate this file
# os.environ["WRITERTOYS_SETTINGS"] = "secret_config.py"
from app import app
app.run(debug=True)

