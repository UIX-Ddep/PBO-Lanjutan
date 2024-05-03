from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return "<p> Hello Dewa Dwi Eka Putra</p>"

@app.route("/template")
def template():
    return render_template('template.html')

@app.route("/hello")
def hello():
    name = request.args.get('name')
    return render_template('hello.html', name=name)