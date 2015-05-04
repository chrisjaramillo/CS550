'''
Created on Feb 23, 2015

@author: Christopher Jaramillo
'''
from NPuzzle import NPuzzle
from utils import *
from searchspace import Explored
from searchspace import Node
from searchspace import print_nodes
from TileBoard import TileBoard

def graph_search(problem, debug=False):
    initState = TileBoard(problem.n, problem.initial)
    initialNode = Node(problem, initState)
    frontier = PriorityQueue()
    frontier.append(initialNode)
    done = found = False
    explored = Explored()
    solution = None
    while not done:
        node = frontier.pop()
        explored.add(node.state)
        if node.state.solved():
            found = done = True
            solution = node
        else:
            actions = problem.actions(node.state)
            for action in actions:
                #print 'Previous state:'
                #print node.__repr__()
                #print 'Applying action ' + str(action)
                newState = node.problem.result(node.state, action)
                #print 'New state:'
                newNode = Node(problem, newState, node, action)
                #print newNode.__repr__()
                #discard = raw_input('press enter')
                if not explored.exists(newState):
                    frontier.append(newNode)
                    explored.add(newNode.state)
        frontierLen = frontier.__len__()
        if frontierLen == 0:
            done = True
    print 'Found a solution from initial state:'
    print initialNode.__repr__()
    print 'Using path: ' + str(solution.solution())
    print 'Solution found:'
    print solution.__repr__()
    return solution  
            
        