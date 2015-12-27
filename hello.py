import os
from flask import Flask, jsonify, request
import requests
from my_keys import *
app = Flask(__name__)
#app.debug = True

## make sure to add your cx and api keys
#cx = ****
#api_key = ****

@app.route('/')
def hello():
	return 'Hello World'

@app.route('/image', methods=['POST'])
def returnJson():
	#make json
	request_data = request.form.get('text')
	imageUrl = getImage(request_data)
	#return it
	return jsonify(response_type='in_channel',text=imageUrl)

def getImage(request_data):
	url = 'https://www.googleapis.com/customsearch/v1?q=' + request_data + '&cx=' + cx + '&safe=medium&searchType=image&key=' + api_key
	goog_search = requests.get(url)
	response = goog_search.json()
	first_image_url = response['items'][0]['link']
	return first_image_url

# only for testing
#app.run()