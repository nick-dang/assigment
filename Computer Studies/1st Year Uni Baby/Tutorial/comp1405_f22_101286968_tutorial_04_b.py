#101286968 
#Nick Dang 
#Description: Play guessing with user. Program generatate # between 1 & 100 (inclusive) and user 
#has 10 guesses. After each incorrect guess, program must report if that user's value is higher or 
 
from random import randint

actualValue = randint(1,100)

counter =0

while counter < 10:
    userGuess = int(input("Please enter your guess: "))

    if userGuess == actualValue:
        print("YOU GUESSED THE CORRECT NUMBER!")
        exit()
    else:
        if userGuess < actualValue:
            print("You number's lower than actual value")
        else:
            print("Your number's higher than the actual value")
    counter+=1

print("You lost. The correct number's", actualValue)