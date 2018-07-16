from flask import Flask
app = Flask(__name__, static_folder = "public")

@app.route('/<name>', methods = ['POST', 'PUT'])    
 
def hello(name):
    return app.send_static_file('main.html')

