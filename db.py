from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    account_id = db.Column(db.Integer, unique=False, nullable=True)
    jobs_submitted = db.Column(db.Integer, unique=False, nullable=False)
    jobs_completed = db.Column(db.Integer, unique=False, nullable=False)
    computer_rating = db.Column(db.Float, unique=False, nullable=True)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float, unique=False, nullable=True)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    files = db.Column(db.String(80), unique=True, nullable=False)
    est_hours = db.Column(db.Float, unique=False, nullable=False)
    payout = db.Column(db.Float, unique=False, nullable=False)

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    files = db.Column(db.String(80), unique=True, nullable=False)
    validated = db.Column(db.Boolean, unique=False, nullable=False)
