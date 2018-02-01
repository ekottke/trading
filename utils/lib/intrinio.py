from utils.api import apiConnector

class intrinioApi(apiConnector):
    def __init__(self,parent):
        super(intrinioApi, self).__init__(parent)


    def initScreen(self,config):
        self.url = 'https://api.intrinio.com/securities/search?'
        if config is not None:
            if 'parameters' in config:
            	self.config['request_url'] = self.config['url'] + 'conditions=' + self.config['parameters']
        elif self.config:
            if 'parameters' in self.config:
                self.config['request_url'] = self.url + 'conditions=' + self.config['parameters']

        data = apiConnector.callApi(self, config=None)

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
