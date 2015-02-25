'''
Created on Feb 22, 2015

@author: Christopher Jaramillo
'''
from Representation import Problem

class NPuzzle(Problem):
    '''
    classdocs
    '''
    
    def __init__(self, n, force_state=None, **kwargs):
        '''
        Constructor
        '''
        super(NPuzzle, self).__init__(force_state, **kwargs)
        self.n = n
    
    def result(self, state, action):
        return state.move(action)