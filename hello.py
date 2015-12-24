import os
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['POST'])
def returnJson():
	#make json
	#request.query_string
	theText = "Hello!"
	#return it
	return jsonify(response_type='in_channel',text=theText)
