'''
Created on Mar 12, 2015

@author: Christopher
'''
import AbstractStrategy

class Strategy(AbstractStrategy.Strategy):
    '''
    classdocs
    '''
    def __init__(self, player, game, maxplies):
        super(Strategy, self).__init__(player, game, maxplies)
        
    def utility(self, board):
        print 'utility'
    def play(self, board):
        print 'play'