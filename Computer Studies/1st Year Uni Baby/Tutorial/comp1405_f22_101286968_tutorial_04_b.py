#101286968 
#Nick Dang 
#Description: Play guessing with user. Program generatate # between 1 & 100 (inclusive) and user 
#has 10 guesses. After each incorrect guess, program must report if that user's value is higher or lower than actual value
 
from random import randint

#generate random 1 < # < 100
actualValue = randint(1,100)

#counter to count amount of times user guesses
counter =0

#check if # of guesses isn't over 10
while counter < 10:
    userGuess = int(input("Please enter your guess: ")) #promt user
    
    #check if user's guess is correct 
    if userGuess == actualValue:
        #print if correct and exit
        print("YOU GUESSED THE CORRECT NUMBER!")
        exit()
    else: #else compared their value with actual value
        if userGuess < actualValue: #check if it's lower 
            print("You number's lower than actual value")
        else: #check it's higher
            print("Your number's higher than the actual value")
    
    #count amount of guesses
    counter+=1

print("You lost. The correct number's", actualValue)