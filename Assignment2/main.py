'''
Created on Feb 24, 2015

@author: Christopher Jaramillo
'''

from GraphSearch import graph_search
from NPuzzle import NPuzzle
from depth_first import *
from breadth_first import *
from manhattan import *

def main():
    n = 8
    print 'Breadth first search'
    pbreadth = NPuzzle(n, g=breadth_first.g, h=breadth_first.h)
    graph_search(pbreadth)
    
    print 'Depth first search'
    pbreadth = NPuzzle(n, g=depth_first.g, h=depth_first.h)
    graph_search(pbreadth)
    
    print 'Manhattan'
    pbreadth = NPuzzle(n, g=manhattan.g, h=manhattan.h)
    graph_search(pbreadth)

if __name__ == '__main__':
    main()