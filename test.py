import logging

def initHistorical(config):
    url = 'https://api.intrinio.com/historical_data?'
    
    if 'start_date' not in config:
        logging.debug('Start Date is not present')
        exit

initHistorical(config={'end_date':'2017-01-01'})