from utils.api import apiConnector
from utils.research import research
from ignore.config import global_config

from datetime import datetime, timedelta
import pdb

class traderApp(object):
    def __init__(self,config):
        self.global_config = global_config
        self.now = datetime.now()
        self.today_str = self.now.strftime('%Y-%m-%d')
        self.trail_30 = self.now - timedelta(days=30)
        self.trail_30_str = self.trail_30.strftime('%Y-%m-%d')
        self.trail_5 = self.now - timedelta(days=5)
        self.trail_5_str = self.trail_5.strftime('%Y-%m-%d')

        self.api = apiConnector(self.global_config)
        self.research = research(self)
        self.analysis = None
        self.trading = None
            
    def updateConfig(self,config,scope):
        if scope is not None:
            if scope == 'global':
                self.global_config.update(config)
        else:
            self.config.update(config)
        