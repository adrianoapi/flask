from flask import Flask, request, jsonify
app = Flask(__name__, static_folder = "public")

@app.route('/<name>', methods = ['GET','POST', 'PUT'])    
 
def hello(name):
    return jsonify(name = name)

