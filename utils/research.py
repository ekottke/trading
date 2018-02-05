from utils.lib.intrinio import intrinioApi
from ignore.config import global_config

import json
import pdb

class research(object):

    def __init__(self, global_app):
        self.api = global_app.api
    
    def screenStocks(self,global_app,config):
        if 'service' in config:
            if config['service']=='intrinio':
                content = global_app.api.intrinio._screener(
                            app=global_app,
                            config=config
                            )
        
    	if config['json']:
    		content = json.loads(content)

    	return content

    def backfillHistoricals(self,global_app,stocks,config):
        if 'service' in config:
            if config['service']=='intrinio':
                historicals = global_app.api.intrinio._backfillHistoricals(
                                app=global_app,
                                stocks=stocks,
                                config=config
                                )

        else:
            historicals = None
            
        return historicals
        
    # def exchangeInfo(self,config):
    #     content = research.buildApiConnector(self,config).initExchangeData(self)
    #
    #     if self.config['json']:
    #         content = json.loads(content)
    #
    #     return content
