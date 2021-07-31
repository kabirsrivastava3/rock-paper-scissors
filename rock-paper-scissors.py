
import random

def playGame():
    inputUser = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n")
    computer = random.choice(['R', 'P', 'S'])

    if inputUser == computer:
        return 'It\'s a tie'

    #R > S, S > P, P > R
    if checkWin(inputUser, computer):
        return 'Yay!! You won!'

    return 'Hah! You lost!!'

def checkWin(humanPlayer, aiOpponent):
    # return true if player wins
    #R > S, S > P, P > R
    if (humanPlayer == 'R' and aiOpponent == 'S') or (humanPlayer == 'S' and aiOpponent == 'P') \
        or (humanPlayer == 'P' and aiOpponent == 'R'):
        return True

print(playGame())
