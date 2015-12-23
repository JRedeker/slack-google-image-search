import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def login():
	#make json
	json = {
		'here is something': 'something'
	}
	#return json
	return json
