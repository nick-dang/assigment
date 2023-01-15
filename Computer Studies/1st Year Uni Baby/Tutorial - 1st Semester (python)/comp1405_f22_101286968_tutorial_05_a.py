#101286968  
#nick Dang
#description: check if a number is prime number and allow user to keep using the program 
#until they want to quit 



def prime(a):
    if (a <= 1):# check if number entered is smaller or equal to 1
        return False

    for i in range (2, a):# Check from 2 to a
        if (a%i == 0): #check if number has a remainder of 0, if yes, that means it has a factor another other than 1 and itself
            return False
    
    return True

 
while True:
    user = int(input("Enter a number: "))
    if prime(user):
        print("The number",user,"is a prime number." )
    else:
        print("The number",user,"isn't a prime number." )
    
    if input("Want to quit? (Y/N) ") == "Y".lower():
        break