import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def returnJson():
	#make json
	#return it
	return jsonify(response_type='in_channel',text='https://i.imgur.com/7drHiqrh.jpg')
