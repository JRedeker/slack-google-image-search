import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def returnJson():
	#make json
	json = jsonify(text='Yo i got dis',attachments=[text='and this'])
	#return json
	return json
