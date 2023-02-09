# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    """
    #use a stack and set 
    fringe = util.Stack()
    visited = []
    
    #set of actions that will be returned
    actionList = []
    
    #store the first position and action
    fringe.push((problem.getStartState(), actionList))
    
    #while the fringe is not empty, keep looping
    while fringe:
    #store the top value of the stack 
    	currentState, actions = fringe.pop()
    	#check if the state was already visited
    	if not currentState in visited:
    		visited.append(currentState)#if not then add it to the visited set
    		if problem.isGoalState(currentState):#check if pacman reach the goal state
    			return actions
    		#find all the node adjacent to the current coordinates
    		for neighbor in problem.getSuccessors(currentState):
    			nextState, action, stepCost = neighbor #each neightbor will hold 3 values
    			nextActions = actions + [action]
    			fringe.push((nextState, nextActions)) #push the adjacent cordinates and actions
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    visited = []
    actionList = []
    fringe = util.Queue()
    
    fringe.push((problem.getStartState(), actionList))
    #while the fringe is not empty
    while fringe:
    	#pop the first item in the queue that returns coordinates and an action
    	currentState, actions = fringe.pop()
    	#check if the coordinates have never been visited
    	if not currentState in visited:
    		#if not then add them to the visited array
    		visited.append(currentState)
    		#check if it is the goal state
    		if problem.isGoalState(currentState):
    			return actions
    		#check all the positions around Pacman and store them in the fringe queue
    		for neightbor in problem.getSuccessors(currentState):
    			nextState, action, stepCost = neightbor
    			nextActions =  actions + [action]
    			fringe.push((nextState, nextActions))
    		
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    visited = []
    actionList = []
    fringe = util.PriorityQueue()
    
    fringe.push((problem.getStartState(), actionList), problem)
    
    while fringe:
    	currentState, actions = fringe.pop()
    	if not currentState in visited:
    		visited.append(currentState)
    		if problem.isGoalState(currentState):
    			return actions
    		for neightbor in problem.getSuccessors(currentState):
    			#find the next actions cost which determines their priority in the queue
    			nextState, action, stepCost = neightbor
    			nextActions =  actions + [action]
    			nextCost = problem.getCostOfActions(nextActions)
    			fringe.push((nextState, nextActions), nextCost)
    		
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    visited = []
    actionList = []
    fringe = util.PriorityQueue()
    
    fringe.push((problem.getStartState(), actionList), heuristic(problem.getStartState(), problem))
    
    while fringe:
    	currentState, actions = fringe.pop()
    	if not currentState in visited:
    		visited.append(currentState)
    		if problem.isGoalState(currentState):
    			return actions
    		for neightbor in problem.getSuccessors(currentState):
    			#calculate the cost of the action plus the heuristic value
    			#the result determines their priority in the queue
    			nextState, action, stepCost = neightbor
    			nextActions =  actions + [action]
    			nextCost = problem.getCostOfActions(nextActions) + heuristic(nextState, problem)
    			fringe.push((nextState, nextActions), nextCost)
    		
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
