'''
Created on Sep 6, 2011

@author: Alex
'''

class PilotState:
    def switchState(self, state):
        assert state is Idle or Active or Death
        
        self.__class__ = state

    def getState(self):
        return self.__class__

class Death(PilotState):
    def isInactive(self):
        return True
        
    
class Idle(PilotState): 
    def __init__ (self, maxlife=20):
        self.life = 0
       
    def addTime(self, time):
        self.life += time

    def getTime(self):
        return self.life

class Active(PilotState): 
    def __init__(self):
        self.life = 0
        
    def addTime(self, time):
        self.life+=time

    def getTime(self):
        return self.life
    
class Pilot:
    def __init__(self):
        self.idle = Idle
        self.active = Active
        self.currentState = self.idle()
        
    def getState(self):
        return self.currentState.getState()
    
    def switchState(self, state):
        self.currentState.switchState(state)

    def addTime(self, time):
        self.currentState.addTime(time)

    def getTime(self):
        return self.currentState.getTime()
    
    def kill(self):
        self.currentState.switchState(Death)
        return self.currentState.getTime()

    
