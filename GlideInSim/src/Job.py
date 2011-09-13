'''
Created on Sep 6, 2011

@author: Alex
'''

class Job(object):
    '''
    classdocs
    '''

    def __init__(self, life=0, idle=True):
        self.life=life
        self.idle=idle
        
    def activate(self):
        self.idle = False
        
    def addtime(self, time):
        self.life+time
        
    def report(self):
        return 

    