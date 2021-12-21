def playGame():
    global numberOfRolls

    player1Pos = 7
    player2Pos = 5

    player1Score = 0
    player2Score = 0

    while True:
        rolls = rollDice() + rollDice() + rollDice()
        player1Pos = player1Pos + rolls
        player1Pos = player1Pos % 10
        if player1Pos == 0:
            player1Pos = 10

        player1Score = player1Score + player1Pos
        
        if player1Score >= 1000:
            break

        rolls = rollDice() + rollDice() + rollDice()
        player2Pos = player2Pos + rolls
        player2Pos = player2Pos % 10
        if player2Pos == 0:
            player2Pos = 10

        player2Score = player2Score + player2Pos
        
        if player2Score >= 1000:
            break
        
    losingScore = min(player1Score, player2Score)

    result = losingScore * numberOfRolls
    print("Result is " + str(result))
    
numberOfRolls = 0
diceValue = 0
def rollDice():
    global diceValue
    global numberOfRolls

    numberOfRolls += 1
    diceValue += 1
    
    if diceValue == 101:
        diceValue = 1

    return diceValue


playGame()