__author__ = 'akashjeez'

import os, sys, json, requests
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/')
def index():
	return 'AkashJeez | Python Flask Docker | Index Page!'


@app.route('/about')
def about():
	return 'AkashJeez | Python Flask Docker | About Page!'


@app.route('/bitcoin/price')
def bitcoin_price():
	try:
		dataset, BASE_URL = [], 'https://api.blockchain.info/charts'
		category = request.args.get('category', default = 'market-price', type = str)
		timespan = request.args.get('timespan', default = '30days', type = str)
		if category.casefold() == 'market-price':
			response = requests.get(f'{BASE_URL}/market-price?timespan={timespan}&format=json').json()
		elif category.casefold() == 'blocks-size':
			response = requests.get(f'{BASE_URL}/blocks-size?timespan={timespan}&format=json').json()
		return jsonify(results = {
			'name': response.get('name', 'TBD').title(), 
			'unit': response.get('unit', 'TBD').title(), 
			'period': response.get('period', 'TBD').title(), 
			'description': response.get('description', 'TBD').title(),
			'data': [ {'date': datetime.fromtimestamp(data['x']).strftime('%d-%m-%Y'), 
				'value': data.get('y', 0)} for data in response['values']]
		}), 200
	except Exception as ex:
		return jsonify( results = { 'Error' : ex } ), 400


@app.route('/bitcoin/exchange')
def bitcoin_exchange():
	try:
		dataset, BASE_URL = [], 'https://api.blockchain.info'
		code = request.args.get('code', default = 'USD', type = str)
		value = request.args.get('value', default = 500, type = int)
		response_1 = requests.get(f'{BASE_URL}/ticker').json()
		response_2 = requests.get(f'{BASE_URL}/tobtc?currency={code.upper()}&value={str(value)}').json()
		return jsonify(results = { 
			'count': len(response_1), 'data': response_1 , 
			'from_currency': code.upper(),'to_currency': 'BTC', 
			'value': int(value), 'price': response_2
		}), 200
	except Exception as ex:
		return jsonify( results = { 'Error' : ex } ), 400


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True)
