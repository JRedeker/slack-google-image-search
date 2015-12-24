import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def returnJson():
	#make json
	#request.query_string
	theText = request
	#return it
	return jsonify(response_type='in_channel',text=theText)
