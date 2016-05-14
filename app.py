#!venv/bin/python
import os
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

# important: remove debug before deployment
if __name__ == "__main__":
    app.run(debug=True)
