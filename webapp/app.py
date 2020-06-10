__author__ = 'akashjeez'

import os, sys, json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Index Page!"

@app.route('about')
def about():
	return "About Page!"

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 4321, debug = True)