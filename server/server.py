import json
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

from flask import Flask, request, jsonify
from flask_api import status

import sqlite3
from sqlite3 import Error


con = sqlite3.connect('mydb.db')
cur = con.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


@app.route('/')
def index():
    return 'hello world'


@app.route('/api/login', methods=['POST'])
def login():
	record = json.loads(request.data)
	username = record['username']
	password = record['password']
	
	cur.execute('SELECT password FROM user WHERE username=?', [username])

	result = cur.fetchone()

	if not result or not check_password_hash(result[0], password):
		result = {"status": status.HTTP_406_NOT_ACCEPTABLE, "desc": "Login Failed"}
		return result

	hash = generate_password_hash(username+password)
	result1 = {
		"status": status.HTTP_200_OK,
		"hash": hash,
		"date": str(date.today().day) + "-" + str(date.today().month) + "-" + str(date.today().year),
		"APIv": "0.1.0"
		}
	return jsonify(result1)

if __name__ == '__main__':
    app.run(debug=True)
