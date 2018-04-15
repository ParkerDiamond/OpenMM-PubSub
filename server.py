from flask import Flask
from flask import jsonify
from flask import request
import flask_uploads
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

'''USERS:

   username
   password
   account_id
   jobs_submitted
   jobs_completed
   computer_rating'''


'''register():
   
   Expects to receive a JSON dictionary with key/values:
   {username: STRING, password: STRING, account_id: INT}'''

@app.route("/register", methods=['POST'])
def register():
    if request.headers['Content-Type'] == 'application/json':
        user = request.json
        user['jobs_submitted'] = 0
        user['jobs_completed'] = 0
        user['computer_rating'] = -1.0
        
        response = jsonify(user)
        response.status_code = 200
        return response
    else:
        return "Error: Bad Content Type"

'''JOBS:

    id = (Integer)
    files (String(80))
    est_hours (Float)
    payout (Float)'''


@app.route("/post_job", methods=['POST'])
def post_job():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        user = data['user']
        job = data['job']
        #Check if user/pass is valid
        #Check if user has sufficient funds
    
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
