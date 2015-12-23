import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def returnJson():
	#make json
	the_attachments = jsonify(text='and this!')
	json = jsonify(text='Yo i got dis',attachments=the_attachments)
	#return json
	return json
