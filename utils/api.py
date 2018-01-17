import urllib2
import json
from pprint import pprint
import pdb
import logging
import datetime

class apiConnector(object):
    def __init__(self,parent):
        if isinstance(parent,object):
            config = parent.config
        elif parent
        if 'username' in parent:
            self.username = config['username']
        if 'password' in config:
            self.password = config['password']
        if 'credentials' in config:
            self.credentials = config['credentials']
        if 'parameters' in config:
            self.parameters = config['parameters']
        elif hasattr(self,'config'):
            if hasattr(self,'config'):
                pass
        
        self.now = datetime.datetime.now()
        self.today_str = self.now.strftime('%Y-%m-%d')
        
    def callApi(self,config):
        
        pdb.set_trace()
        if config is not None:
        	if 'headers' in config:
        		request_headers = config['headers']
        	if 'url' in config:
        		request_url = config['url']
        	if 'data' in config:
        		data = config['data']
        else:
            if hasattr(self,'data'):
                data = self.data
            else:
                data = None
                
            if hasattr(self,'headers'):
                request_headers = self.headers
            else:
                request_headers = None
                
            if hasattr(self,'request_url'):
                request_url = self.request_url
            elif hasattr(self,'url'):
                request_url = self.url
            else:
                return 'A URL endpoint is required to make an HTTP call'
        
        if request_headers:
        	request = urllib2.Request(request_url, headers=request_headers)
        else:
            request = urllib2.Request(request_url)
            
        contents = urllib2.urlopen(request,data).read()

    	return contents
	
class intrinioApi(apiConnector):
    def __init__(self,parent):
        super(intrinioApi, self).__init__(parent)
            

    def initScreen(self,config):
        self.url = 'https://api.intrinio.com/securities/search?'
        
        if config is not None:
            if 'parameters' in config:
            	self.request_url = self.url + 'conditions=' + config['parameters']
        elif self.parameters:
            self.request_url = self.url + self.parameters

        data = apiConnector.callApi(self,config)

        return data
        
    # def initExchangeData(self,config):
#         pdb.set_trace()
#         self.url = 'https://api.intrinio.com/prices/exchange?'
#         if 'type' in self.config:
#             if config['type']=='forex':
#                 pass
#             elif config['type']=='stock':
#                 if 'symbols' in config:
#                     for s in config['symbols']:
#                         self.url += 'identifier='+s+'price_date='+self.today_str
#
#                         data = apiConnector.callApi(self,config)
#
#                         return data
#                 else:
#                     return 'At least one stock symbol is required'
#         else:
#             return 'Please specify what exchange data you want'
#
#     def initBackfill(config):
#         self.url = 'https://api.intrinio.com/historical_data?'
#         if 'symbols' in config:
#             config = {}
#             for s in config['symbols']:
#                 data = apiConnector.callApi(self,config)
#
#     def initHistorical(config):
#         self.url = 'https://api.intrinio.com/historical_data?'
#
#         if 'start_date' not in config:
#             logger.debug('Start Date is not present')
#             exit