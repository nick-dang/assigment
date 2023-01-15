#101286968  
#nick Dang
#description: a simple game of rock-paper-scissor or tic tac toe

from random import choice

def rps(a): #rock paper and scissor game
    computer = ["rock", "paper", "scissor"] #randomize for computer 
    computerChoice = choice(computer)
    if a.lower() == computerChoice: #when it's tie 
        return print("Tie.")
    elif a.lower() == "rock" and computerChoice == "paper": #when user is rock and computer is paper 
        return print ("You lose. Computer play paper")
    elif a.lower() == "rock" and computerChoice == "scissor": #when user is rock and comp is scissor 
        return print ("You win! Computer play scissor")
    elif a.lower() == "paper" and computerChoice == "rock": #when user is paper and comp is rock
        return print ("You win! Computer play rock.")
    elif a.lower() == "paper" and computerChoice == "scissor": #when user is paper and comp is scissor 
        return print ("You lose. Computer plays scissor")
    elif a.lower() == "scissor" and computerChoice == "rock": #when user is scissor and compt is rock
        return print ("You lose. Computer plays rock")
    elif a.lower() == "scissor" and computerChoice == "paper": #when user is scissor and compt is paper
        return print ("You win! Computer plays paper")


def main():
    user = input("Rock, Paper, Scissor: ")
    rps(user)


main()