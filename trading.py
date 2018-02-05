import datetime
from utils.application import traderApp

import pdb

now = datetime.datetime.now()
end_date = now.strftime('%Y-%m-%d')
start_date = (now - datetime.timedelta(days=7)).strftime('%Y-%m-%d')


app = traderApp(
    config=None
)

stocks = app.research.screenStocks(
    app,
	config = {
		'service':'intrinio',
		'json':True,
		'parameters': {
		    'conditions':'close_price~lt~5.00~penny_stock,pricetoearnings~lt~50~penny_stock'
		}
    }
)

# print stocks

backdata = app.research.backfillHistoricals(
    app,
    stocks['data'],
    config={
        'service':'intrinio',
        'json':True,
        'parameters':{
            'start_date':'2018-01-01',
            'end_date':'2018-01-14',
            'frequency':'daily'   
        }
    }
)

print backdata

"""

data_bf = r.backfillHistoricals(
    config={
        'service':'intrinio',
        'json':True,
        'params': '',
        'start_date': start_date,
        'end_date': end_date,
        'symbols': data_r['data']
    }
)
"""
