from utils.api import apiConnector, intrinioApi
from config import global_config
import json
from pprint import pprint
import pdb

def prepConfig(config):
	if config['service'] is not None:
		local_config = global_config[config['service']].copy()
	else:
		local_config = global_config['default'].copy()
	
	local_config.update(config)
	return local_config

def screenStocks(config):
	local_config = prepConfig(config)
	if 'service' in config:
		if config['service']=='intrinio':
			connector = intrinioApi(local_config)
			content = connector.initScreen(local_config)
	else:
		connector = apiConnector(local_config)

	if local_config['json']:
		content = json.loads(content)
		
	return content

def backfillHistoricals(config):
	local_config = prepConfig(config)
	connector = apiConnector(local_config)
	
	for t in local_config['tickers']:
		local_config['params'] = ''
		content = connector.callApi(
						config=local_config
					)

	if local_config['json']:
		content = json.loads(content)
	
	return content