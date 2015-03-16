'''
Created on Mar 12, 2015

@author: Christopher
'''

import AI
import Human
import checkerboard
import Tonto

def Game(red=AI.Strategy, black=Tonto.Strategy, init=None, maxplies=8, verbose=False):
    sharedBoard = checkerboard.CheckerBoard()
    redplayer = red('r',checkerboard.CheckerBoard(), maxplies)
    blackplayer = black('b',checkerboard.CheckerBoard(), maxplies)
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
        if not gameComplete:
            if move == []:
                gameComplete = True
                if (moveCount % 2) == 0:
                    winner = 'r'
                else:
                    winner = 'b'
    print sharedBoard
    if winner is None:
        print 'tie'
    else:
        print 'The winner is: ' + winner