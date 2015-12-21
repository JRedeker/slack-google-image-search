import os
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World'

app.route('/images', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        result = {
        	"response_type": "in_channel",
        	"text": "this is the message"
        }
        return result
    else:
        return