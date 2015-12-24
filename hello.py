import os
from flask import Flask, jsonify, request
app = Flask(__name__)
#app.debug = True

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
	url = "nothing"
	return url

app.run()