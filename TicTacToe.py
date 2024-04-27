import os
import random
import sys
from termcolor import colored, cprint
import time

playAgain = "s"
plays = 0
playerToPlay = 2
maxPlays = 9
gameWin = "n"
# the blank spaces are meant to be filled with the player's symbol to preserve the format
ticTacToe = [
    [" ", " ", " ",],
    [" ", " ", " ",],
    [" ", " ", " "]
]

def screen():
    # can be declared as global, but not necessary
    global ticTacToe
    global plays

    os.system("cls")

    # building the game board
    print("   0   1   2")
    print("0:  " + ticTacToe[0][0] + " | " + ticTacToe[0][1] + " | " + ticTacToe[0][2])
    print("  -------------")
    print("1:  " + ticTacToe[1][0] + " | " + ticTacToe[1][1] + " | " + ticTacToe[1][2])
    print("  -------------")
    print("2:  " + ticTacToe[2][0] + " | " + ticTacToe[2][1] + " | " + ticTacToe[2][2])

    playsCollored = colored('Plays: ', 'yellow') + colored(str(plays), 'yellow')
    print(playsCollored)

# screen()

# gameplay
# PLAYER (P2) CPU (P1)
def playerPlays():
    global plays
    global playerToPlay
    global maxPlays

    if playerToPlay == 2 and plays < maxPlays:
        playerPlaysColored = colored('Player plays', 'green')
        print(playerPlaysColored)
        row    = int(input("Row    = "))
        column = int(input("Column = "))

        if row < 0 or row > 2 or column < 0 or column > 2:
            invalidPlayColored = colored('Invalid play', 'red')
            print(invalidPlayColored)
            playerPlays()

        if ticTacToe[row][column] == " ":
            ticTacToe[row][column] = "X"
            playerToPlay = 1
            plays += 1

        else:
            invalidPositionColored = colored('Invalid position', 'red')
            print(invalidPositionColored)
            playerPlays()

def cpuPlays():
    global plays
    global playerToPlay
    global maxPlays

    if playerToPlay == 1 and plays < maxPlays:
        time.sleep(1)
        row    = random.randint(0, 2)
        column = random.randint(0, 2)

        if ticTacToe[row][column] == " ":
            ticTacToe[row][column] = "O"
            playerToPlay = 2
            plays += 1
        else:
            cpuPlays()

def checkWin():
    global ticTacToe
    global gameWin

    # check rows
    for i in range(3):
        if ticTacToe[i][0] == ticTacToe[i][1] == ticTacToe[i][2] and ticTacToe[i][0] != " ":
            if ticTacToe[i][0] == "X":
                gameWin = "player"
                # print("Player wins")
                return gameWin
            else: 
                if ticTacToe[i][0] == "O":
                    gameWin = "cpu"
                    # print("CPU wins")
                    return gameWin

    # check columns
    for i in range(3):
        if ticTacToe[0][i] == ticTacToe[1][i] == ticTacToe[2][i] and ticTacToe[0][i] != " ":
            if ticTacToe[i][0] == "X":
                gameWin = "player"
                # print("Player wins")
                return gameWin
            else: 
                if ticTacToe[i][0] == "O":
                    gameWin = "cpu"
                    # print("CPU wins")
                    return gameWin
        
    # check diagonals
    for i in range(3):
        if ticTacToe[0][0] == ticTacToe[1][1] == ticTacToe[2][2] and ticTacToe[0][0] != " ":
            if ticTacToe[i][0] == "X":
                    gameWin = "player"
                    # print("Player wins")
                    return gameWin
            else: 
                if ticTacToe[i][0] == "O":
                    gameWin = "cpu"
                    # print("CPU wins")
                    return gameWin
                

# restart the game

def restartGame():
    global plays
    global playerToPlay
    global maxPlays
    global gameWin
    global ticTacToe

    plays = 0
    playerToPlay = 2
    maxPlays = 9
    gameWin = "n"
    ticTacToe = [
        [" ", " ", " ",],
        [" ", " ", " ",],
        [" ", " ", " "]
    ]
    gameLoop()
                
# finish the game

def gameOver():
    gameOverCollored = colored('Game Over', 'magenta')
    print(gameOverCollored)

    if gameWin == "player":
        playerWinsColored = colored('Player wins', 'green')
        print(playerWinsColored)   
    if gameWin == "cpu":
        cpuWinsColored = colored('CPU wins', 'blue')
        print(cpuWinsColored)
    if plays == maxPlays:
        drawColored = colored('Draw', 'yellow')
        print(drawColored)
    playAgain()

def playAgain():
    playOption = input("Play again? (Y/N) ")
    if playOption == "Y" or playOption == "y":
        restartGame()
    if playOption == "N" or playOption == "n":
        sys.exit()
    else:
        print("Invalid option")
        playAgain()

# in game loop

def gameLoop():
    while True:
        if checkWin() == "player" or checkWin() == "cpu" or plays == maxPlays:
            break
        screen()
        playerPlays()
        screen()
        if checkWin() == "player" or checkWin() == "cpu" or plays == maxPlays:
            break
        cpuPlays()
        screen()
    gameOver()

# call the game loop

gameLoop()