# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood().asList()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        score = 0
        #If it's a food great which is really important here.
        if (currentGameState.getFood()[newPos[0]][newPos[1]]):
            score +=1

        #calculate all the distance to food less it is it's better.
        current_food = newPos
        for food in newFood:
            #return the nearest_food using the below line.
            nearest_food = min(newFood, key=lambda x: manhattanDistance(x, current_food))
            score += 1.0/manhattanDistance(nearest_food, current_food)
            newFood.remove(nearest_food)
            current_food = nearest_food

        #ghost distances if less than some basic return large negative value
        if ( min([manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]) == 1):
            return -1000

        #add the Score as well.
        score += successorGameState.getScore()

        return score

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """

        pacman_legal_actions = gameState.getLegalActions(0) #all the legal actions of pacman.
        max_value = float('-inf')
        max_action  = None #one to be returned at the end.

        for action in pacman_legal_actions:   #get the max value from all of it's successors.
            action_value = self.Min_Value(gameState.generateSuccessor(0, action), 1, 0)
            if ((action_value) > max_value ): #take the max of all the children.
                max_value = action_value
                max_action = action

        return max_action #Returns the final action .

    def Max_Value (self, gameState, depth):
        """For the Max Player here Pacman"""

        if ((depth == self.depth)  or (len(gameState.getLegalActions(0)) == 0)):
            return self.evaluationFunction(gameState)

        return max([self.Min_Value(gameState.generateSuccessor(0, action), 1, depth) for action in gameState.getLegalActions(0)])


    def Min_Value (self, gameState, agentIndex, depth):
        """ For the MIN Players or Agents  """

        if (len(gameState.getLegalActions(agentIndex)) == 0): #No Legal actions.
            return self.evaluationFunction(gameState)

        if (agentIndex < gameState.getNumAgents() - 1):
            return min([self.Min_Value(gameState.generateSuccessor(agentIndex, action), agentIndex + 1, depth) for action in gameState.getLegalActions(agentIndex)])

        else:  #the last ghost HERE
            return min([self.Max_Value(gameState.generateSuccessor(agentIndex, action), depth + 1) for action in gameState.getLegalActions(agentIndex)])

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """

        alpha = float('-inf') #max best option on path to root
        beta = float('inf') #min best option on path to root

        action_value = float ('-inf')
        max_action = None
        for action in gameState.getLegalActions(0):
            action_value = self.Min_Value(gameState.generateSuccessor(0, action), 1, 0, alpha, beta)
            if (alpha < action_value):
                alpha = action_value
                max_action = action

        return max_action

    def Min_Value (self, gameState, agentIndex, depth, alpha, beta):
        """ For Min agents best move """

        if (len(gameState.getLegalActions(agentIndex)) == 0): #No Legal actions.
            return self.evaluationFunction(gameState)

        action_value = float('inf')
        for action in gameState.getLegalActions(agentIndex):
            if (agentIndex < gameState.getNumAgents() - 1):
                action_value = min(action_value, self.Min_Value(gameState.generateSuccessor(agentIndex,action), agentIndex + 1, depth, alpha, beta))
            else:  #the last ghost HERE
                action_value = min(action_value, self.Max_Value(gameState.generateSuccessor(agentIndex, action), depth + 1, alpha, beta))

            if (action_value < alpha):
                return action_value
            beta = min(beta, action_value)

        return action_value

    def Max_Value (self, gameState, depth, alpha, beta):
        """For Max agents best move"""

        if (depth == self.depth or len(gameState.getLegalActions(0)) == 0):
            return self.evaluationFunction(gameState)

        action_value = float('-inf')
        for action in gameState.getLegalActions(0):
            action_value = max(action_value, self.Min_Value(gameState.generateSuccessor(0, action), 1, depth, alpha, beta))

            if (action_value > beta):
                return action_value
            alpha = max(alpha, action_value)

        return action_value


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        pacman_legal_actions = gameState.getLegalActions(0) #all the legal actions of pacman.
        max_value = float('-inf')
        max_action  = None #one to be returned at the end.

        for action in pacman_legal_actions:   #get the max value from all of it's successors.
            action_value = self.Min_Value(gameState.generateSuccessor(0, action), 1, 0)
            if ((action_value) > max_value ): #take the max of all the children.
                max_value = action_value
                max_action = action

        return max_action #Returns the final action .

    def Max_Value (self, gameState, depth):
        """For the Max Player here Pacman"""

        if ((depth == self.depth)  or (len(gameState.getLegalActions(0)) == 0)):
            return self.evaluationFunction(gameState)

        return max([self.Min_Value(gameState.generateSuccessor(0, action), 1, depth) for action in gameState.getLegalActions(0)])


    def Min_Value (self, gameState, agentIndex, depth):
        """ For the MIN Players or Agents  """

        num_actions = len(gameState.getLegalActions(agentIndex))

        if (num_actions == 0): #No Legal actions.
            return self.evaluationFunction(gameState)

        if (agentIndex < gameState.getNumAgents() - 1):
            return sum([self.Min_Value(gameState.generateSuccessor(agentIndex, action), agentIndex + 1, depth) for action in gameState.getLegalActions(agentIndex)]) / float(num_actions)

        else:  #the last ghost HERE
            return sum([self.Max_Value(gameState.generateSuccessor(agentIndex, action), depth + 1) for action in gameState.getLegalActions(agentIndex)]) / float(num_actions)


def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: Inverse sums of nearest food distances and capsule distances, adding game score,
      subtracting ghost distance and remaining food. 
    """

    GhostStates = currentGameState.getGhostStates() #all the ghost states
    Pacman_Pos = currentGameState.getPacmanPosition()
    food_list = (currentGameState.getFood()).asList() #get all the food as list.
    capsule_list = currentGameState.getCapsules() #get all the capsules.
    no_food = len(food_list)
    no_capsule = len(capsule_list)

    state_score = 0 #initializing to zero.

    #Feature 1 no of Legalactions: Not working well
    #state_score += len(currentGameState.getLegalPacmanActions())/40.0

    #Feature 2 distances from ghosts if exists
    if currentGameState.getNumAgents() > 1:
        ghost_dis = min( [manhattanDistance(Pacman_Pos, ghost.getPosition()) for ghost in GhostStates])
        if (ghost_dis <= 1):
            return -10000
        state_score -= 1.0/ghost_dis

    #Feature 3 food positions
    current_food = Pacman_Pos
    for food in food_list:
        closestFood = min(food_list, key=lambda x: manhattanDistance(x, current_food))
        state_score += 1.0/(manhattanDistance(current_food, closestFood))
        current_food = closestFood
        food_list.remove(closestFood)

    #Feature 4 capsule positions
    current_capsule = Pacman_Pos
    for capsule in capsule_list:
        closest_capsule = min(capsule_list, key=lambda x: manhattanDistance(x, current_capsule))
        state_score += 1.0/(manhattanDistance(current_capsule, closest_capsule))
        current_capsule = closest_capsule
        capsule_list.remove(closest_capsule)

    #Feature 4 Score of the game
    state_score += 8*(currentGameState.getScore())

    #Feature 5: remaining food and capsule
    state_score -= 6*(no_food + no_capsule)

    return state_score

# Abbreviation
better = betterEvaluationFunction
