'''
Created on Mar 12, 2015

@author: Christopher
'''
import AbstractStrategy
from checkerboard import CheckerBoard

class Strategy(AbstractStrategy.Strategy):
    '''
    classdocs
    '''
    def __init__(self, player, game, maxplies):
        super(Strategy, self).__init__(player, game, maxplies)
        
    def alphaBetaSearch(self, board):
        startAlpha = float('-inf')
        startBeta = float('inf')
        v, alpha, move = self.maxValue(board, startAlpha, startBeta)
        print 'Chose move: ' + str(move) + ' with value: ' + str(v) 
        return move

    def maxValue(self, board, alpha, beta, plies=0):
        move = None
        terminal, winner = board.is_terminal()
        if terminal or plies == self.maxplies:
            return self.utility(board), alpha, move
        else:
            v = float('-inf')
            for action in reversed(board.get_actions(self.maxplayer)):
                retval, beta, aMove = self.minValue(board.move(action), alpha, beta, plies+1)
                if v < retval:
                    v = retval
                    move = action
                if v >= beta:
                    break
                else:
                    alpha = max(alpha, v)
            return v, alpha, move
        
    def minValue(self, board, alpha, beta, plies=0):
        move = None
        terminal, winner = board.is_terminal()
        if terminal or plies == self.maxplies:
            return self.utility(board), beta, move
        else:
            v = float('inf')
            for action in board.get_actions(self.minplayer):
                retval, alpha, aMove = self.maxValue(board.move(action), alpha, beta, plies+1)
                if v > retval:
                    v = retval
                    move = action
                if v <= alpha:
                    break
                else:
                    beta = max(beta, v)
            return v, beta, move
        
    def utility(self, board):
        terminal, winner = board.is_terminal()
        if terminal:
            if winner is self.maxplayer:
                return 200
            else:
                return -200
        else:
            return self.evaluate(board)

    def evaluate(self, board):
        pieceCount = 0
        kingCount = 0 

        playerIndex = CheckerBoard.playeridx(self.maxplayer)
        for row, column, piece in board:
            playeridx, king = CheckerBoard.identifypiece(piece)
            if playeridx == playerIndex:
                pieceCount += 1
                if king:
                    kingCount += 1
            else:
                pieceCount -= 1
                if king:
                    kingCount -= 1
        return pieceCount +  (2*kingCount) 
        
    def play(self, board):
        print 'AI is thinking...'
        move = self.alphaBetaSearch(board)
        if move != None:
            return board.move(move), move
        else:
            return board, []