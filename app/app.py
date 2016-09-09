from flask import Flask, url_for, json, request
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
def api_names():
    gender = request.args.get('gender', '')
    if not gender:
        gender = 'any'
    number = request.args.get('number', '')
    if not number:
        number = "1" # remember this is a string
    return url_for('api_names') + " called with gender \"" + gender + "\" and number \"" + number + "\""

if __name__ == '__main__':
    app.run()
