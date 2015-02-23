'''
Created on Feb 22, 2015

@author: Christopher Jaramillo
'''
from Representation import Problem
from TileBoard import TileBoard

class NPuzzle(Problem):
    '''
    classdocs
    '''
    
    def __init__(self, n, force_state=None, **kwargs):
        '''
        Constructor
        '''
        super(NPuzzle, self).init(force_state, **kwargs)
        self.tileBoard = TileBoard(n, force_state=force_state)
    
    def result(self, state, action):
        return state.move(action)