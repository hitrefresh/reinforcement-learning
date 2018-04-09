from modules.BoardState import *
import pickle

# AI player
class Player:
    # @stepSize: step size to update estimations
    # @exploreRate: possibility to explore
    def __init__(self, allStates, stepSize=0.1, exploreRate=0.03, applyExplorationUpdates=False):
        self.allStates = allStates
        self.estimations = dict()
        self.stepSize = stepSize
        self.epoch = 0.0
        self.exploreRate = exploreRate
        self.states = []
        self.exploratoryStates = []
        self.id = 0
        self.applyExplorationUpdates = applyExplorationUpdates

    def savePolicy(self):
        fw = open('optimal_policy_' + str(self.symbol), 'wb')
        pickle.dump(self.estimations, fw)
        fw.close()

    def loadPolicy(self):
        fr = open('optimal_policy_' + str(self.symbol), 'rb')
        self.estimations = pickle.load(fr)
        fr.close()

    def reset(self):
        self.states = []

    def updateInitialEstimates(self):
        # Set our initial value estimates for all states.
        for hash in self.allStates.keys():
            (state, isEnd) = self.allStates[hash]
            if isEnd:
                if state.winner == self.symbol:
                    self.estimations[hash] = 1.0
                else:
                    self.estimations[hash] = 0
            else:
                self.estimations[hash] = 0.5

    # symbol can only be -1, or 1.
    def setSymbol(self, symbol):
        self.symbol = symbol
        self.updateInitialEstimates()

    # update estimation according to reward
    def feedReward(self, reward):
        if len(self.states) == 0:
            return
        self.epoch += 1.0
        self.states = [state.getHash() for state in self.states]
        target = reward
        self.exploratoryStates.reverse()
        for index, latestState in enumerate(reversed(self.states)):
            if (not self.exploratoryStates[index]) or (self.applyExplorationUpdates):
                #                 math.sqrt(self.epoch)
                value = self.estimations[latestState] + (self.stepSize) * (target - self.estimations[latestState])
                self.estimations[latestState] = value
                target = value
        self.states = []
        self.exploratoryStates = []

    # determines next action from a state and returns the state resulting from taking that action as well as whether
    # the state taken was exploratory.
    def takeAction(self, state):
        nextStates = []
        nextPositions = []
        for i in range(state.BOARD_ROWS):
            for j in range(state.BOARD_COLS):
                if state.data[i, j] == 0:
                    nextPositions.append([i, j])
                    nextStates.append(state.nextState(i, j, self.symbol).getHash())
        if np.random.binomial(1, self.exploreRate):
            np.random.shuffle(nextPositions)
            action = nextPositions[0]
            action.append(self.symbol)
            nextstate = NextState(state, action[0], action[1], self.symbol)
            return nextstate, True

        values = []
        for hash, pos in zip(nextStates, nextPositions):
            values.append((self.estimations[hash], pos))
        np.random.shuffle(values)
        values.sort(key=lambda x: x[0], reverse=True)
        action = values[0][1]
        action.append(self.symbol)
        nextState = NextState(state, action[0], action[1], self.symbol)
        return nextState, False

    def addStateToFeedbackPath(self, state, isExploratory):
        self.states.append(state)
        self.exploratoryStates.append(isExploratory)