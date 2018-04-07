from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/register", methods=['POST'])
def register():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        username = data['username']
        password = data['password']
        
        response = jsonify({'u':username,'p':password})
        response.status_code = 200
        return response
    else:
        return "Error: Bad Content Type"

@app.route("/post_job", methods=['POST'])
def post_job():
    pass

@app.route("/get_job", methods=['POST'])
def get_job():
    pass

@app.route("/post_results", methods=['POST'])
def post_results():
    pass

@app.route("/get_results", methods=['POST'])
def get_results():
    pass
