'''
Created on Mar 12, 2015

@author: Christopher
'''
import AbstractStrategy
from operator import or_

class Strategy(AbstractStrategy.Strategy):
    '''
    classdocs
    '''
    def __init__(self, player, game, maxplies):
        super(Strategy, self).__init__(player, game, maxplies)
        
    def alphaBetaSearch(self, board):
        startAlpha = float('-inf')
        startBeta = float('inf')
        bestMove = None
        bestValue = 0
        for action in board.get_actions(self.maxplayer):
            value, alpha = self.maxValue(board, startAlpha, startBeta, action)
            if value > bestValue:
                bestValue = value
                bestMove = action 
        return bestMove

    def maxValue(self, board, alpha, beta, action, plies=0):
        board = board.move(action)
        terminal, winner = board.is_terminal()
        if terminal or plies == self.maxplies:
            return self.utility(board, winner, board.playeridx(self.maxplayer)), alpha
        else:
            v = float('-inf')
            for action in board.get_actions(self.maxplayer):
                retval, beta = self.minValue(board, alpha, beta, action, plies+1)
                v = max(v, retval)
                if v >= beta:
                    break
                else:
                    alpha = max(alpha, v)
            return v, alpha
        
    def minValue(self, board, alpha, beta, action, plies=0):
        board = board.move(action)
        terminal, winner = board.is_terminal()
        if terminal or plies == self.maxplies:
            return self.utility(board, winner, board.playeridx(self.minplayer)), beta
        else:
            v = float('inf')
            for action in board.get_actions(self.minplayer):
                retval, alpha = self.maxValue(board, alpha, beta, action, plies + 1) 
                v = min(v, retval)
                if v <= alpha:
                    break
                else:
                    beta = min (beta, v)
            return v, beta
        
    def utility(self, board, winner, playerIndex):
        if winner == self.maxplayer:
            return 1
        elif winner == self.minplayer:
            return 0
        else:
            return self.evaluate(board, playerIndex)

    def evaluate(self, board, playerIndex):
        totalValue = 0
        for piece in board:
            pidx, isKing = board.identifypiece(piece)
            if pidx == playerIndex:
                if isKing:
                    totalValue += 2
                else:
                    totalValue += 1
        return totalValue
        
    def play(self, board):
        move = self.alphaBetaSearch(board)
        print 'AI has chosen move: ' + str(move)
        return board.move(move), move