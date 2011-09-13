'''
Created on Sep 6, 2011

@author: Alex
'''

class PilotState:
    def switchState(self):
        raise NotImplementedError()
    def getState(self):
        raise NotImplementedError()
    
class Idle(PilotState):
    def switchState(self):
        self.__class__ = Active
    def getState(self):
        return self.__class__

class Active(PilotState):
    def SwitchState(self):
        self.__class__ = Idle
    def getState(self):
        return self.__class__
    
class Pilot:
    def __init__(self):
        self.idle = Idle()
        self.active = Active()
        self.currentState = self.idle
    
    def getState(self):
        return self.idle.getState()
        
    def switchState(self):
        self.currentState.switchState()
    
if __name__ == '__main__':
    x = Pilot()
    x.getState()
    x.switchState()