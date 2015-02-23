'''
Created on Feb 23, 2015

@author: Christopher
'''
from NPuzzle import NPuzzle

def graph_search(problem, debug=False):
    '''
    From in class notes on search
    frontier = problem.initial_state() # priority queue based on lowest cost
    done = found = False
    explored = {} # keep track of nodes we have checked
    while not done
        node = frontier.get_node() # remove state
        explored = union(explored, node)
        if node in problem.goals()
            found = done = True
        else
            # only add novel results from the current node
            nodes = setdiff(results from actions(node), union(frontier,explored))
            for n in nodes
            estimate a cost g’(n) + h’(n)
            frontier.add_nodes(nodes) # merge new nodes in by estimated cost
        done = frontier.is_empty()
    return solution if found else return failure
    '''
    