import urllib2
import json
from pprint import pprint
import pdb
import logging
import datetime

class apiConnector(object):
    def __init__(self,parent):
        if isinstance(parent,object):
            self.config = parent.config
        elif type(parent) is dict:
            if 'username' in parent:
                self.username = parent['username']
            if 'password' in parent:
                self.password = parent['password']
            if 'credentials' in parent:
                self.credentials = parent['credentials']
            if 'parameters' in parent:
                self.parameters = parent['parameters']
            elif hasattr(self,'config'):
                if hasattr(self,'config'):
                    pass

        self.now = datetime.datetime.now()
        self.today_str = self.now.strftime('%Y-%m-%d')

    def callApi(self,config):

        if config is None and hasattr(self,'config'):
            config = self.config

    	if 'headers' in config:
    		request_headers = config['headers']

    	if 'data' in config:
    		data = config['data']
        else:
            data = None

        if 'request_url' in config:
            request_url = config['request_url']
        elif 'url' in config:
            request_url = config['url']
        else:
            return 'A URL endpoint is required to make an HTTP call'

        if request_headers:
        	request = urllib2.Request(request_url, headers=request_headers)
        else:
            request = urllib2.Request(request_url)

        contents = urllib2.urlopen(request,data).read()

    	return contents