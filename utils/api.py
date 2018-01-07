import urllib2
import json
from pprint import pprint
import pdb

class apiConnector(object):
	def __init__(self,config):
		if 'username' in config:
			self.username = config['username']
		if 'password' in config:
			self.password = config['password']
		if 'credentials' in config:
			self.credentials = config['credentials']
		if 'params' in config:
			self.params = config['params']
	def callApi(self,config):
		if 'headers' in config:
			request_headers = config['headers']
		else:
			request_headers = None
		if 'url' in config:
			request_url = config['url']
		elif hasattr(self,'request_url'):
			request_url = self.request_url
		elif hasattr(self,'url'):
			request_url = self.url
		if 'data' in config:
			data = config['data']
		else:
			data = None
		
		request = urllib2.Request(request_url, headers=request_headers)
		contents = urllib2.urlopen(request,data).read()
		
		return contents
		
class intrinioApi(apiConnector):
	def __init__(self,config):
		super(intrinioApi, self).__init__(config)
	
	def initScreen(self,config):
		self.url = 'https://api.intrinio.com/securities/search?'
		if 'params' in config:
			self.request_url = self.url + 'conditions=' + config['params']
		else:
			self.request_url = self.url
		
		data = apiConnector.callApi(self,config)
		
		return data
	
	def initBackfill(config):
		if config['type']=='backfill':
			self.url = 'https://api.intrinio.com/historical_data?'