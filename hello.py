import os
import urllib2
import simplejson
import cStringIO
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

def getImage(request_data):
	fetcher = urllib2.build_opener()
	searchTerm = 'parrot'
	startIndex = 0
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + startIndex
	f = fetcher.open(searchUrl)
	deserialized_output = simplejson.load(f)
	imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
	#file = cStringIO.StringIO(urllib.urlopen(imageUrl).read())
	return imageUrl