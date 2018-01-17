class dbConnector(object):
    def __init__(self,config):
        if 'username' in config:
            self.username = config['username']
        else:
            print 'You must have a username to access the database'
            exit
        
        if 'password' in config:
            self.password = config['password']
        else:
            print 'You must have a password to access the database'
            exit
            
    