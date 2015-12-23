import os
from flask import Flask, json
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def returnJson():
	#make json
	data = {
		"response_type": "in_channel",
		'text' : 'https://i.imgur.com/7drHiqrh.jpg'
	}
	#return
	return json.dumps(data)
