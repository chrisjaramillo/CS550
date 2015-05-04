'''
Created on Feb 22, 2015

@author: Christopher Jaramillo
'''

class depth_first():
    def __init__(self):
        '''
        Constructor
        '''
    @classmethod
    def g(cls, parentnode, action, childnode):
        '''
        '''
        return parentnode.get_g()-1
        
    
    @classmethod
    def h(cls, state):
        '''
        '''
        return 0