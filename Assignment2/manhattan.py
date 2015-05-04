'''
Created on Feb 22, 2015

@author: Christopher Jaramillo
'''

class manhattan():
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        
    @classmethod
    def g(cls, parentnode, action, childnode):
        '''
        '''
        return parentnode.get_g()+1
    
    @classmethod
    def h(cls, state):
        '''
        '''
        middle = (state.boardsize-1) / 2
        r, c = state.empty
        moves = abs(r-middle)+abs(c-middle)
        return moves
        