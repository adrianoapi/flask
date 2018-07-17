from flask import Flask, request, jsonify, render_template, abort, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder = "public")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/flask"
db = SQLAlchemy(app)

class User(db.Model):
    id       = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(120))
    
    def __init__(self, username, password):
        slef.username = username
        self.password = password
        

@app.route('/<name>', methods = ['GET','POST', 'PUT'])    
def hello(name):
    users = User.query.all()
    return jsonify(users = users)

@app.route('/')
def root():
    return "index"

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404