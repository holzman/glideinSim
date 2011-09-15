

'''@author: Alex'''

import collections
import Pilot


class Site(object):
    '''
    classdocs
    '''
    def __init__(self, qlength):     
        self.jobs = collections.deque(maxlen=qlength)
        self.finished = list()
        
    def addjob(self):
        self.jobs.put(Pilot())

    def process(self):pass
    
        
        
    