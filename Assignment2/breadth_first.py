'''
Created on Feb 22, 2015

@author: cxj8923
'''

import SearchStrategy
from searchspace import Node

class breadth_first(SearchStrategy):
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
        return 0