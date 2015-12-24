import os
import urllib2
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['POST'])
def returnJson():
	#make json
	#request.query_string
	request_data = request.form.get('text')
	imageUrl = getImage(request_data)
	#return it
	return jsonify(response_type='in_channel',text=imageUrl)
	#return jsonify(response_type='in_channel',text=imageUrl)

def getImage(request_data):
	url = 'https://www.googleapis.com/customsearch/v1?q=' + request_data
	goog_request = requests.get(url)
	#goog_results = goog_results.json()
	#imageUrl = goog_results
	return request_data