import datetime
from research import research

import pdb

now = datetime.datetime.now()
end_date = now.strftime('%Y-%m-%d')
start_date = (now - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

r = research(
	config = {
		'service':'intrinio',
		'json':True,
		'parameters': 'close_price~lt~5.00~penny_stock,pricetoearnings~lt~50~penny_stock'
	})

e = research(
	config = {
		'service':'intrinio',
		'json':True,
		'type': 'stock'
	})

data_r = r.screenStocks(config=None)
print data_r['data']


#data_e = e.exchangeInfo(config=None)
#print data_e



# backfillHistoricals(
#     config={
#         'service':'intrinio',
#         'json':True,
#         'params': '',
#         'start': start_date,
#         'end': end_date,
#         'symbols': data['data']
#     }
# )
