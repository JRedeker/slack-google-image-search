import os
import json
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def returnJson():
	#make json
	data = {
		'text':'Yo i got dis',
		'attachments': {
			'text':'and this!'
		}
	}
	json = json.dumps(data)
	#return json
	return json
