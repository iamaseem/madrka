from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

utxt = open("user.txt", "r")
ptxt = open("pass.txt", "r")

@app.route('/api/login', methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['password']
    i = 0
    data = "failed"
    lines = utxt.readlines()
    while i<len(lines):
        line = lines[i].rstrip('\n')
        if user == line:
            all_pass = ptxt.readlines()
            pas =  all_pass[i].rstrip('\n')
            if password == pas:
                data = "success"
            else:
                data = "failed"
        i = i+1

    return data

app.run(debug=True)