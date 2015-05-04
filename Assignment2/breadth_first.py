'''
Created on Feb 22, 2015

@author: Christopher Jaramillo
'''

class breadth_first():
    '''
    classdocs
    '''


    def __init__(self):
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
    