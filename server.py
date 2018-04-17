from flask import Flask
from flask import jsonify
from flask import request
import flask_uploads
from flask_sqlalchemy import SQLAlchemy
from db import User, Job

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

    try:
        if request.headers['Content-Type'] == 'application/json':
            user = request.json
            user['jobs_submitted'] = 0
            user['jobs_completed'] = 0
            user['computer_rating'] = -1.0
        
            if User.query.filter_by(username=user['username']).first():
                response = jsonify({'Error': 'Username already taken'})
                response.status_code = 409
                return response
            else:
                newUser = User(username=user['username'],
                               password=user['password'],
                               account_id=user['account_id'],
                               jobs_submitted=user['jobs_submitted'],
                               jobs_completed=user['jobs_completed'],
                               computer_rating=user['computer_rating'])
                db.session.add(newUser)
                db.session.commit()

                response = jsonify(user)
                response.status_code = 200
                return response
        else:
            response = jsonify({'Error': 'Please use Content-Type "application/json"'})
            response.status_code = 415
            return response
    except KeyError as ex:
        response = jsonify({'Error': str(ex)})
        response.status_code = 400
        return response
        

'''JOBS:

    id = (Integer)
    files (String(80))
    est_hours (Float)
    payout (Float)'''

@app.route("/post_job", methods=['POST'])
def post_job():

    ''' Users will need to provide their username and password in
        the payload in order to post a job. They also need to specify
        the payout amount which cannot exceed the amount in their account.'''

    try:
        if request.headers['Content-Type'] == 'multipart/form-data':
            data = request.json
            username = data['username']
            password = data['password']
            job_files = request.files['job_files']
            est_hours = data['est_hours']
            payout = data['payout']
        else:
            response = jsonify({'Error': 'Please use Content-Type "multipart/form-data"'})
            response.status_code = 415
            return response
    except KeyError as ex:
        response = jsonify({'Error': str(ex)})
        response.status_code = 400
        return response

@app.route("/get_job", methods=['POST'])
def get_job():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json 
    pass

@app.route("/post_results", methods=['POST'])
def post_results():
    pass

@app.route("/get_results", methods=['POST'])
def get_results():
    pass

