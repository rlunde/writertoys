from flask import Flask, url_for, json, request
from crossdomain import crossdomain
import logging
from logging.handlers import RotatingFileHandler
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'cli'))
import randnames

app = Flask(__name__)

# stolen from Jonathan Tushman's: http://flask.pocoo.org/snippets/117/
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)
    
    return '\n<br/>'.join(output)

@app.route('/')
def api_root():
    return "This is the writertoys REST interface. Use /routes endpoint to see which endpoints are available"

@app.route('/routes')
def api_routes():
    return list_routes()

@app.route('/names')
@crossdomain(origin='*')
def api_names():
    gender = request.args.get('gender', '')
    if not gender:
        gender = 'any'
    number = request.args.get('number', '')
    if not number:
        number = "1" # remember this is a string
    app.logger.info(url_for('api_names') + " called with gender \"" + gender + "\" and number \"" + number + "\"")
    return generate_names(gender, number)

def generate_names(gender, number):
    rval = ""
    for n in range(0,int(number)):
        first_name = randnames.generate_name(gender, 'first')
        last_name = randnames.generate_name(gender, 'last')
        full_name = first_name + " " + last_name
        rval = rval + full_name + "<br/>"
    return rval

if __name__ == '__main__':
    # TODO: figure out what we want to do for logging
    randnames.load_names() # cache stuff
    handler = RotatingFileHandler('writertoys.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host='localhost',port=5000)
