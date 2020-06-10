__author__ = 'akashjeez'

from app import app
import os, sys, unittest


class AppTestCase(unittest.TestCase):
	''' Test Case for this Python Flask Web App!'''

	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/')
		assert 'Index Page!' in response.data

	def test_about(self):
		tester = app.test_client(self)
		response = tester.get('/about')
		assert 'About Page!' in response.data


if __name__ == '__main__':
	unittest.main()