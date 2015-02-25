'''
Created on Feb 22, 2015

@author: cxj8923
'''

class SearchStrategy(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    @classmethod
    def g(cls, parentnode, action, childnode):
        raise NotImplementedError
    
    @classmethod
    def h(cls, state):
        raise NotImplementedError