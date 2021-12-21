
class GameState:
    def __init__(self,p1Pos, p2Pos, p1Score, p2Score):
        self.positions = []
        self.positions.append(p1Pos)
        self.positions.append(p2Pos)
        self.scores = []
        self.scores.append(p1Score)
        self.scores.append(p2Score)

def playGame():
    wins = []
    wins.append(0)
    wins.append(0)

    diceProbs = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

    gameStates = {}
    ngs = GameState(7,5,0,0)
    gameStates[ngs] = 1
    step = 0

    while len(gameStates) > 0:
        step += 1
        newgamestates  = {}

        for i in gameStates:
            if step%2 == 1:
                for rollValue in diceProbs:
                    newPosition = (i.positions[0] + rollValue - 1) % 10 +1
                    newScore = i.scores[0]+newPosition
                    if newScore >= 21:
                        wins[0] += gameStates[i]*diceProbs[rollValue]
                    else:
                        ngs = GameState(newPosition, i.positions[1], newScore, i.scores[1])
                        newgamestates[ngs] = gameStates[i]*diceProbs[rollValue]
            else:
                for rollValue in diceProbs:
                    newPosition = (i.positions[1] + rollValue - 1) % 10 +1
                    newScore = i.scores[1]+newPosition
                    if newScore >= 21:
                         wins[1] += gameStates[i]*diceProbs[rollValue]
                    else:
                        ngs = GameState(i.positions[0], newPosition, i.scores[0], newScore)
                        newgamestates[ngs] = gameStates[i]*diceProbs[rollValue]

        gameStates = newgamestates
        print("{} {} {} {}".format(step, wins[0], wins[1], len(gameStates)))

    result = max(wins[0], wins[1])
    print("Result is " + str(result))

def diceRate(rollValue):
    if rollValue == 3:
        return 1

    if rollValue == 4:
        return 3

    if rollValue == 5:
        return 6

    if rollValue == 6:
        return 7

    if rollValue == 7:
        return 6

    if rollValue == 8:
        return 3

    if rollValue == 9:
        return 1

    return 0


playGame()