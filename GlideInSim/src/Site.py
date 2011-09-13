

'''@author: Alex'''

import Queue
import types


class Cycle:
    def __init__(self, jobs, time):
        self.endcycle = False
        assert jobs > 0 and type(jobs) is types.IntType, "parameter must be a positive integer"
        assert time > 0 and type(time) is types.IntType, "parameter must be a positive integer"
        self.elapsed = 0 
        self.time = time
        self.jobs = jobs
        
    def increment(self, x):
        self.elapsed += float(self.time)/self.jobs #time elapsed per job
        return self.elapsed

    

if __name__ == '__main__':
    jobs=0
    elapsed = Cycle(5,1)
    while jobs < 15:  
        elapsed.increment()
        jobs +=1

class Site(object):
    '''
    classdocs
    '''
    def __init__(self, jobs,qlength):     
        self.jobs = Queue.Queue(self.qlength)
        

    
        
        
    