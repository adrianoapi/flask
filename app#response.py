from flask import Flask, request, jsonify
app = Flask(__name__, static_folder = "public")

@app.route('/<name>', methods = ['GET','POST', 'PUT'])    
 
def hello(name):
    return jsonify( name    = name,
                    email   = ['sdcomputadores@gmail.com','adrianoapi@hotmail.com',
                        {
                            'name'   : 'Adriano A Costa',
                            'company': 'Microsoft'
                        }
                    ],
                    
                    addres  = {
                        'street': "Rua Marambai",
                        'number': 158,
                        'city'  : "Sao Paulo",
                        'state' : "SP"
                    })

