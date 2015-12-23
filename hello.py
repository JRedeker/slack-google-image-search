import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['GET'])
def returnJson():
	#make json
	json = jsonify(text=['Yo i got dis'],attachments=['https://media3.giphy.com/media/rl0FOxdz7CcxO/200_s.gif'])
	#return json
	return json
