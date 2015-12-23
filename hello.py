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
		'text' : 'Yo I got dis',
		'attachments' : [
			{
				'text' : 'and this!'
			}
		]
	}
	#return
	return json.dumps(data)
