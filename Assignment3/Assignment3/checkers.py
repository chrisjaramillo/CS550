'''
Created on Mar 12, 2015

@author: Christopher
'''

import AI
import Human
import checkerboard

def Game(red=AI.Strategy, black=Human.Strategy, init=None, maxplies=8, verbose=False):
    redplayer = red('r',checkerboard.CheckerBoard, maxplies)
    blackplayer = black('b',checkerboard.CheckerBoard, maxplies)

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        