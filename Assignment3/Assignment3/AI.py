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
        #terminal, winner = board.is_terminal()
        #if terminal:
        #    if winner is self.maxplayer:
        #        return 20000000
        #    else:
        #        return -20000000
        #else:
        return self.evaluate(board)

    def evaluate(self, board):
        pieceCount = self.totalPieces(board)
        kingCount = self.totalKings(board) 
        distanceToKing = self.distanceToKings(board)
        pieceDefense = self.pieceDefense(board)
        edgePieces = self.edgePieces(board)
        return pieceCount + kingCount + distanceToKing + edgePieces + pieceDefense
    
    def totalPieces(self, board):
        pieces = 0
        playerIndex = CheckerBoard.playeridx(self.maxplayer)
        for row, column, piece in board:
            playeridx, king = CheckerBoard.identifypiece(piece)
            if playeridx == playerIndex:
                pieces += 1
            else:
                pieces -= 1
        return pieces
    
    def edgePieces(self, board):
        pieces = 0
        playerIndex = CheckerBoard.playeridx(self.maxplayer)
        for row, column, piece in board:
            playeridx, king = CheckerBoard.identifypiece(piece)
            if playeridx == playerIndex:
                if row is 0 or column is 0 or row is 7 or column is 7:
                    pieces += 10
                if king:
                    if (row is 0 and column is 0) or (row is 0 and column is 7) or (row is 7 and column is 0) or (row is 7 and column is 7):
                        pieces += 100
            else:
                if row is 0 or column is 0 or row is 7 or column is 7:
                    pieces -= 1
                if (row is 0 and column is 0) or (row is 0 and column is 7) or (row is 7 and column is 0) or (row is 7 and column is 7):
                    pieces -= 1
        return pieces
    
    def totalKings(self, board):
        kings = 0
        playerIndex = CheckerBoard.playeridx(self.maxplayer)
        for row, column, piece in board:
            playeridx, king = CheckerBoard.identifypiece(piece)
            if playeridx == playerIndex:
                if king:
                    kings += 1
            else:
                if king:
                    kings -= 1
        return kings
                
    def distanceToKings(self, board):
        distance = 0
        playerIndex = CheckerBoard.playeridx(self.maxplayer)
        for row, column, piece in board:
            playeridx, king = CheckerBoard.identifypiece(piece)
            if playeridx == playerIndex:
                if not king:
                    distance -= board.disttoking(self.maxplayer, row)
            else:
                if not king:
                    distance += board.disttoking(self.minplayer, row)
        return distance
    
    def pieceDefense(self, board):
        defense = 0
        playerIndex = CheckerBoard.playeridx(self.maxplayer)
        for row, column, piece in board:
            playeridx, king = CheckerBoard.identifypiece(piece)
            if playeridx == playerIndex:
                if not king:
                    defense += self.positionDefense(board, row, column)
                    defense += self.kingDefense(board, row, column)
            else:
                if not king:
                    defense -= self.positionDefense(board, row, column)
                    defense -= self.kingDefense(board, row, column)                                
        return defense
    
    def positionDefense(self, board, row, column):
        '''
        The pieces here are asking if they are defended
        black is looking for pieces in higher number rows
        red is looking for pieces in lower number rows
        '''
        defense = 0
        left = None
        right = None
        matches = None
        if  self.maxplayer is 'r':
            left = [-1, -1]
            right = [-1, 1]
            matches = ['r', 'R']
        else:
            left = [1 ,-1]
            right = [1, 1]
            matches = ['b', 'B']
        leftRow = row + int(left[0])
        leftColumn = column + int(left[1])
        rightRow = row + int(right[0])
        rightColumn = column + int(right[1])
        
        if board.onboard(leftRow, leftColumn):
            if board.board[leftRow][leftColumn] in matches:
                defense +=1
        if board.onboard(rightRow, rightColumn):
            if board.board[rightRow][rightColumn] in matches:
                defense +=1
        return defense
    
    def kingDefense(self, board, row, column):
        '''
        the pieces here are asking if there are peices behind them to defend kings
        black is looking for pieces in lower number rows
        red is looking for pieces in higher number rows
        '''
        defense = 0
        left = None
        right = None
        matches = None
        if  self.maxplayer is 'r':
            left = [1, -1]
            right = [1, 1]
            matches = ['r', 'R']
        else:
            left = [-1 ,-1]
            right = [-1, 1]
            matches = ['b', 'B']
        leftRow = row + int(left[0])
        leftColumn = column + int(left[1])
        rightRow = row + int(right[0])
        rightColumn = column + int(right[1])
        
        if board.onboard(leftRow, leftColumn):
            if board.board[leftRow][leftColumn] in matches:
                defense +=1
        if board.onboard(rightRow, rightColumn):
            if board.board[rightRow][rightColumn] in matches:
                defense +=1
        return defense
                        
    def play(self, board):
        print 'AI is thinking...'
        move = self.alphaBetaSearch(board)
        if move != None:
            return board.move(move), move
        else:
            return board, []