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
	if request.headers.getlist("X-Forwarded-For"):
	   ip = request.headers.getlist("X-Forwarded-For")[0]
	else:
	   ip = request.remote_addr
	imageUrl = getImage(request_data,ip)
	#return it
	return jsonify(response_type='in_channel',text=imageUrl)

def getImage(request_data,ip):
	url = 'https://www.googleapis.com/customsearch/v1?q=' + request_data
	goog_request = requests.get(url)
	goog_results = goog_results.json()
	imageUrl = goog_results
	return imageUrl