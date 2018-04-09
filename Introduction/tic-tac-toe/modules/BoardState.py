import numpy as np


class State:
    def __init__(self, BOARD_ROWS=3, BOARD_COLS=3, toPlay=1):
        # the board is represented by a n * n array,
        # 1 represents chessman of the player who moves first,
        # -1 represents chessman of another player
        # 0 represents empty position
        self.data = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.winner = None
        self.hashVal = None
        self.end = None
        self.toPlay = toPlay
        self.BOARD_ROWS = BOARD_ROWS
        self.BOARD_COLS = BOARD_COLS

    def getHash(self):
        """
        Calculate the hash value for one state, it's unique
        :return:
        """
        if self.hashVal is None:
            self.hashVal = 0
            for i in self.data.reshape(self.BOARD_ROWS * self.BOARD_COLS):
                if i == -1:
                    i = 2
                self.hashVal = self.hashVal * 3 + i

            if self.toPlay == 1:
                self.hashVal = self.hashVal * 3 + 1
            else:
                self.hashVal = self.hashVal * 3 + 2
        return int(self.hashVal)

    # determine whether a player has won the game, or it's a tie
    def isEnd(self):
        if self.end is not None:
            return self.end
        results = []
        # check row
        for i in range(0, self.BOARD_ROWS):
            results.append(np.sum(self.data[i, :]))
        # check columns
        for i in range(0, self.BOARD_COLS):
            results.append(np.sum(self.data[:, i]))

        # check diagonals
        results.append(0)
        for i in range(0, self.BOARD_ROWS):
            results[-1] += self.data[i, i]
        results.append(0)
        for i in range(0, self.BOARD_ROWS):
            results[-1] += self.data[i, self.BOARD_ROWS - 1 - i]

        for result in results:
            if result == 3:
                self.winner = 1
                self.end = True
                return self.end
            if result == -3:
                self.winner = -1
                self.end = True
                return self.end

        # whether it's a tie
        sum = np.sum(np.abs(self.data))
        if sum == self.BOARD_ROWS * self.BOARD_COLS:
            self.winner = 0
            self.end = True
            return self.end

        # game is still going on
        self.end = False
        return self.end

    # @symbol 1 or -1
    # put chessman symbol in position (i, j)
    def nextState(self, i, j, symbol):
        newState = State(toPlay=-symbol)
        newState.data = np.copy(self.data)
        newState.data[i, j] = symbol
        self.BOARD_ROWS = newState.BOARD_ROWS
        self.BOARD_COLS = newState.BOARD_COLS
        return newState

    # print the board
    def show(self):
        for i in range(0, self.BOARD_ROWS):
            print('-------------')
            out = '| '
            for j in range(0, self.BOARD_COLS):
                if self.data[i, j] == 1:
                    token = '*'
                if self.data[i, j] == 0:
                    token = '0'
                if self.data[i, j] == -1:
                    token = 'x'
                out += token + ' | '
            print(out)
        print('-------------')


def getAllStatesImpl(currentState, currentSymbol, allStates):
    for i in range(0, currentState.BOARD_ROWS):
        for j in range(0, currentState.BOARD_COLS):
            if currentState.data[i][j] == 0:
                newState = currentState.nextState(i, j, currentSymbol)
                newHash = newState.getHash()
                if newHash not in allStates.keys():
                    isEnd = newState.isEnd()
                    allStates[newHash] = (newState, isEnd)
                    if not isEnd:
                        getAllStatesImpl(newState, -currentSymbol, allStates)


def getAllStates():
    allStates = dict()
    currentState = State(toPlay=1)
    allStates[currentState.getHash()] = (currentState, currentState.isEnd())
    getAllStatesImpl(currentState, currentState.toPlay, allStates)
    currentState = State(toPlay=-1)
    getAllStatesImpl(currentState, currentState.toPlay, allStates)
    return allStates


# Does not check for validity of the insertion!
def NextState(currState, i, j, symbol):
    newState = State(toPlay=-symbol)
    newState.data = np.copy(currState.data)
    newState.data[i, j] = symbol
    return newState