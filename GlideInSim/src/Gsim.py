'''
Created on Sep 4, 2011

@author: Alex
'''
import ConfigParser
import types

    
def main(test):
    print test
    
    
if __name__=="__main__":
    main("hello")
    



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