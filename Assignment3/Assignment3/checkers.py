'''
Created on Mar 12, 2015

@author: Christopher
'''

import AI
import Human
import checkerboard

def Game(red=AI.Strategy, black=Human.Strategy, init=None, maxplies=8, verbose=False):
    sharedBoard = checkerboard.CheckerBoard()
    redplayer = red('r',sharedBoard, maxplies)
    blackplayer = black('b',sharedBoard, maxplies)
    moveCount = 0
    gameComplete = False 
    winner = None
    move = None
    while not gameComplete:
        if (moveCount % 2) == 0:
            sharedBoard, move = redplayer.play(sharedBoard)
        else:
            sharedBoard, move = blackplayer.play(sharedBoard)
        moveCount += 1
        gameComplete, winner = sharedBoard.is_terminal()
    print 'The winner is: ' + winner

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        