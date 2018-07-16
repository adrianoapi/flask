from flask import Flask, request, jsonify, render_template
app = Flask(__name__, static_folder = "public")

@app.route('/<name>', methods = ['GET','POST', 'PUT'])    
 
def hello(name):
    return render_template('hello.html', name = name)
