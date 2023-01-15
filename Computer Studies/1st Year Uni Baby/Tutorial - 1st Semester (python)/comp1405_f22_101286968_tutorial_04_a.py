#101286968 
#Nick Dang 
#Description: ask user for an int and print out the corresepsonding "number triangle".

#ask user for input
userInput = int(input("Enter an integer: "))

#while input isn't between 1 & 9, ask again in loop
while (userInput < 1 or userInput > 9):
    userInput = int(input("Please re-enter an integer between 1 and 9 inclusively: "))

#print the number triangle
for i in range (userInput):
    for j in range (i+1):
        print(i+1, end="")
    print()
    


