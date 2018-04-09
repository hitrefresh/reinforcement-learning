from modules.BoardState import State

class Judger:
    # @player1: player who will move first, its chessman will be 1
    # @player2: another player with chessman -1
    # @feedback: if True, both players will receive rewards when game is end
    def __init__(self, allStates, player1, player2, feedback=True, shuffleFirstPlayer=False):
        self.p1 = player1
        self.p1.playerID = 1
        self.p2 = player2
        self.p2.playerID = 2
        self.feedback = feedback
        self.currentPlayer = None
        self.p1Symbol = 1
        self.p2Symbol = -1
        self.p1.setSymbol(self.p1Symbol)
        self.p2.setSymbol(self.p2Symbol)
        # Player 1 goes first in the first game, then they alternate.
        self.currentState = State(toPlay=1)
        self.allStates = allStates
        self.startPlayer = 1
        self.shuffleFirstPlayer = shuffleFirstPlayer
    # give reward to two players
    def giveReward(self):
        if self.currentState.winner == self.p1Symbol:
            self.p1.feedReward(1)
            self.p2.feedReward(0)
        elif self.currentState.winner == self.p2Symbol:
            self.p1.feedReward(0)
            self.p2.feedReward(1)
        else:
            self.p1.feedReward(0.5)
            self.p2.feedReward(0.5)

    def reset(self):
        self.p1.reset()
        self.p2.reset()
        if self.shuffleFirstPlayer:
            self.startPlayer = -self.startPlayer
        if self.startPlayer == 1:
            self.currentState = State(toPlay=1)
            self.currentPlayer = None
        else:
            self.currentState = State(toPlay=-1)
            self.currentPlayer = None

    # @show: if True, print each board during the game
    def play(self, show=False):
#         self.reset()
        while True:
            # set current player
            if self.currentPlayer == self.p1:
                self.currentPlayer = self.p2
            elif self.currentPlayer == self.p2:
                self.currentPlayer = self.p1
            elif self.startPlayer == 1: # game starting case
#                 print("Game starting with player 1...")
                self.currentPlayer = self.p1
            else:
#                 print("Game starting with player 2...")
                self.currentPlayer = self.p2

            if show:
                self.currentState.show()
            # Current player plays a move.
            nextState, isExploratory = self.currentPlayer.takeAction(self.currentState)
            self.currentPlayer.addStateToFeedbackPath(nextState, isExploratory)

            self.currentState = nextState
            hashValue = self.currentState.getHash()
            self.currentState, isEnd = self.allStates[hashValue]
            if isEnd:
                if self.feedback:
                    self.giveReward()
                return self.currentState.winner