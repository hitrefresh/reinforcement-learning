def train(player1, player2, judger, epochs=10000):
    player1Win = 0.0
    player2Win = 0.0
    player1WinPrev = 0.0
    player2WinPrev = 0.0
    gamesWonP1Per1000 = []
    gamesWonP2Per1000 = []
    for i in range(0, epochs):
        winner = judger.play()
        if winner == 1:
            player1Win += 1
        if winner == -1:
            player2Win += 1
        judger.reset()
        if not (i % 1000):
            gamesWonP1Per1000.append(player1Win - player1WinPrev)
            gamesWonP2Per1000.append(player2Win - player2WinPrev)
            print('Epoch: {0}'.format(i),
                  ", P1 win rate(train): {0}".format((player1Win - player1WinPrev) / 1000),
                  ", P2 win rate(train): {0}".format((player2Win - player2WinPrev) / 1000),
                  end="\r"),
            player1WinPrev = player1Win
            player2WinPrev = player2Win
    print()
    print("P1 win rate(train): ", player1Win / epochs)
    print("P2 win rate(train): ", player2Win / epochs)
    player1.savePolicy()
    player2.savePolicy()
    return gamesWonP1Per1000, gamesWonP2Per1000


def compete(judger, turns=500):
    player1Win = 0.0
    player2Win = 0.0
    for i in range(0, turns):
        if not i%100:
            print('Epoch: {0}'.format(i), end="\r")
        winner = judger.play()
        if winner == 1:
            player1Win += 1
        if winner == -1:
            player2Win += 1
            
        judger.reset()
    print("P1 win rate(compete): ", player1Win / turns)
    print("P2 win rate(compete): ", player2Win / turns)
