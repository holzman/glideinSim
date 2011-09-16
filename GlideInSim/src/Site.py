

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
        self.jobs.append(Pilot())
       

    def process(self):
        self.finished.append(self.jobs.pop())
        
    
    
class Deque(collections.deque):
    def __init__(self, iterable=(), maxlen=None):
        super(Deque, self).__init__(iterable, maxlen)
        self._maxlen = maxlen
    
    def maxlen(self):
        return self._maxlen
    
  
        