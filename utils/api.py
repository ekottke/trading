import urllib2
import json
import datetime
from lib.intrinio import intrinioApi
from ignore.config import global_config

import pdb
import logging

class apiConnector(object):
    def __init__(self,config):
        self.intrinio = intrinioApi(config=config['intrinio'])
    
    def callApi(self,config):
        if config is None:
            raise RuntimeException('Cannot call blank API')
        else:
            # if 'headers' in config:
            #     request_headers = config['headers']

            if 'data' in config:
            	data = config['data']
            else:
                data = None

            if 'url' in config:
                request_url = config['url']
            else:
                raise RuntimeException('A URL endpoint is required to make an HTTP call')

            if 'parameters' in config:
                query_params = ''
                for k in config['parameters']:
                    query_params += k + '=' + config['parameters'][k] + '&'
                request_url += query_params
            
            # pdb.set_trace()
            
            if 'headers' in config:
            	request = urllib2.Request(request_url, headers=config['headers'])
            else:
                request = urllib2.Request(request_url)
    
            contents = urllib2.urlopen(request,data).read()

            return contents