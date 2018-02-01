from utils.lib.intrinio import intrinioApi
from ignore.config import global_config
import json
import pdb

class research(object):

    def __init__(self,config):
        if 'service' in config:
            self.config = global_config[config['service']].copy()
        else:
            self.config = global_config['default'].copy()

        if config is not None:
            self.config.update(config)

        self.api = research.buildApiConnector(self,None)

    @staticmethod
    def buildApiConnector(self,config):
        if config is not None:
            self.updateConfig(config)

    	if self.config['service']:
    		if self.config['service']=='intrinio':
    			connector = intrinioApi(self)
    	else:
    		connector = apiConnector(self.config)

        return connector

    @staticmethod
    def updateConfig(self,config):
        self.config.update(config)

    def screenStocks(self,config):
        content = self.api.initScreen(config)

    	if self.config['json']:
    		content = json.loads(content)

    	return content

    # def exchangeInfo(self,config):
    #     content = research.buildApiConnector(self,config).initExchangeData(self)
    #
    #     if self.config['json']:
    #         content = json.loads(content)
    #
    #     return content


    # def backfillHistoricals(config):
    #
    #     connector = research.buildApiConnector(self,config)
    #     content = connector.initHistorical(self)
    #
    #     for t in local_config['tickers']:
    #         local_config['params'] = ''
    #         content = connector.callApi(
    #                         config=local_config
    #                     )
    #
    #     if local_config['json']:
    #         content = json.loads(content)
    #
    #     return content
