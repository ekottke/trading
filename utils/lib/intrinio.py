import pdb

class intrinioApi(object):
    def __init__(self,config):
        if config is not None:
            self.config = config

    def _screener(self,app,config):
        c = self.config
        c.update({
            'url':'https://api.intrinio.com/securities/search?'
        })
        
        if config is not None:
            c.update(config)
        
        data = app.api.callApi(
                config=c
                )
        
        return data
    
    def _backfillHistoricals(self,app,stocks,config):
        
        if config is not None:
            if 'start_date' in config['parameters']:
                start_date = config['parameters']['start_date']
            else:
                print 'Start Date defaulted'
                start_date = app.trail_30
        
            if 'end_date' in config['parameters']:
                end_date = config['parameters']['end_date']
            else:
                print 'End Date defaulted'
                end_date = app.today_str
    
            if 'frequency' in config['parameters']:
                frequency = config['parameters']['frequency']
            else:
                print 'Frequency defaulted'
                frequency = 'daily'
            
            if 'item' in config['parameters']:
                item = config['parameters']['item']
            else:
                print 'Item defaulted'
                item = 'high_price'
                
        c = self.config
        c.update({
            'url':'https://api.intrinio.com/historical_data?',
            'parameters': {
                'start_date':start_date,
                'end_date':end_date,
                'frequency':frequency,
                'item':item
            }
        })
        
        # pdb.set_trace()
        
        data = dict()
        for s in stocks:
            c['parameters']['identifier']=s['ticker']
            data[s['ticker']]=app.api.callApi(
                                    config=c
                                )
        
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