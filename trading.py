import datetime
from research import screenStocks, backfillHistoricals

import pdb

now = datetime.datetime.now()
end_date = now.strftime('%Y-%m-%d')
start_date = (now - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

data = screenStocks(
	config = {
		'service':'intrinio',
		'json':True,
		'params': 'close_price~lt~5.00~penny_stock,pricetoearnings~gt~10~penny_stock'
	})
	
print data

pdb.set_trace()

backfillHistoricals(
	config={
		'service':'intrinio',
		'json':True,
		'params': '',
		'start': start_date,
		'end': end_date,
		'tickers': data['data']
	}
)