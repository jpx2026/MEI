from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/read-form', methods=['POST', 'GET'])
def read_form():
    data = request.json
    
    resultRes = {   
        'Name': data['Name'],
        'Email': data['Email'],
        'Pass': data['Pass']
    }
    #page = "<html>   <head> <title>MEI - CC - LAb 01</title> </head> <body>  <h1>Laboratory Exercise 01 - Insecure service Response</h1>"
    #page = str(page) + str(resultRes)
    #page = page + "</body></html"
    
    return resultRes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)