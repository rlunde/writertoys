from app import app

@app.route('/')
@app.route('/index')
def index():
    app.send_static_file('index.html')
