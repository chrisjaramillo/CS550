'''
Created on Mar 17, 2015

@author: cxj8923
'''
from checkerboard import CheckerBoard
import AI
import unittest



class Test(unittest.TestCase):

    def testTotalPieces(self):
        testBoard = CheckerBoard()
        redplayer = AI.Strategy('r',CheckerBoard(), 8)
        self.assertEqual(redplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for red starting board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        blackplayer = AI.Strategy('b',CheckerBoard(), 8)
        self.assertEqual(blackplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for red starting board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        testBoard.clearboard()
        testBoard.place(0, 1, 'r')
        testBoard.update_counts()
        self.assertEqual(redplayer.totalPieces(testBoard), 1, 'AI.totalPieces failed for red one piece board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        self.assertEqual(blackplayer.totalPieces(testBoard), -1, 'AI.totalPieces failed for black one piece board. Count was: ' + str(blackplayer.totalPieces(testBoard)))
        testBoard.place(0, 3, 'b')
        testBoard.update_counts()
        self.assertEqual(redplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for red two piece board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        self.assertEqual(blackplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for black two piece board. Count was: ' + str(blackplayer.totalPieces(testBoard)))
        testBoard.place(0, 5, 'R')
        testBoard.update_counts()
        self.assertEqual(redplayer.totalPieces(testBoard), 1, 'AI.totalPieces failed for red three piece board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        self.assertEqual(blackplayer.totalPieces(testBoard), -1, 'AI.totalPieces failed for black three piece board. Count was: ' + str(blackplayer.totalPieces(testBoard)))
        testBoard.place(0, 7, 'B')
        testBoard.update_counts()
        self.assertEqual(redplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for red four piece board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        self.assertEqual(blackplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for black four piece board. Count was: ' + str(blackplayer.totalPieces(testBoard)))
    
    def testEdgePieces(self):
        testBoard = CheckerBoard()
        redplayer = AI.Strategy('r',CheckerBoard(), 8)
        self.assertEqual(redplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for red starting board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        blackplayer = AI.Strategy('b',CheckerBoard(), 8)
        self.assertEqual(blackplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for red starting board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        testBoard.clearboard()
        testBoard.place(0, 1, 'r')
        testBoard.update_counts()
        self.assertEqual(redplayer.totalPieces(testBoard), 1, 'AI.totalPieces failed for red one piece board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        self.assertEqual(blackplayer.totalPieces(testBoard), -1, 'AI.totalPieces failed for black one piece board. Count was: ' + str(blackplayer.totalPieces(testBoard)))
        testBoard.place(0, 3, 'b')
        testBoard.update_counts()
        self.assertEqual(redplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for red two piece board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        self.assertEqual(blackplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for black two piece board. Count was: ' + str(blackplayer.totalPieces(testBoard)))
        testBoard.place(0, 5, 'R')
        testBoard.update_counts()
        self.assertEqual(redplayer.totalPieces(testBoard), 1, 'AI.totalPieces failed for red three piece board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        self.assertEqual(blackplayer.totalPieces(testBoard), -1, 'AI.totalPieces failed for black three piece board. Count was: ' + str(blackplayer.totalPieces(testBoard)))
        testBoard.place(0, 7, 'B')
        testBoard.update_counts()
        self.assertEqual(redplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for red four piece board. Count was: ' + str(redplayer.totalPieces(testBoard)))
        self.assertEqual(blackplayer.totalPieces(testBoard), 0, 'AI.totalPieces failed for black four piece board. Count was: ' + str(blackplayer.totalPieces(testBoard)))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAI']
    unittest.main()