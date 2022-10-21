#Nick Dang
#101286968
#take a value from command-line argument from user and ask for an input 
#and follow the "pipeline" design patern. Final value is converted from 
#float -> int (display) -> char(display)

import sys 

#value from command-line argument 
a = int(sys.argv[1])

#ask user for an integer
b = int(input("Enter a number: "))

#take command-line argument -5 from it, add it to the integer that is one more than itself,**3, 
#add input value, multiply it by 0.012192
c =  int(((2*a-4)**3 + b) *0.012192)

print("Your value is ",c, "\nIt's ", chr(c)," in 'char'")


