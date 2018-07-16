from flask import Flask, request, jsonify, render_template, abort, redirect, url_for

app = Flask(__name__, static_folder = "public")

@app.route('/<name>', methods = ['GET','POST', 'PUT'])    
def hello(name):
    abort(404)
    return redirect(url_for('/'))
    #return render_template('hello.html', name = name)

@app.route('/')
def root():
    return "index"

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404