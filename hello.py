import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def login():
	returnJson()

def returnJson():
	#make json
	json = jsonify(answer=['this is answer'])
	#return json
	return json
