#101286968
#nick dang
#description: ask user for an int then transform the list into containing 'n' random ints. Use loops to allow user to replace the #s inside
#list with a specified string. Count how many times specified string by user appears in the list. 

from random import randint



user_list = [] #empty list 

user_int = int(input("Please enter an int for list: ")) 

#method to count a particular string
def string_to_count():
    counter = 0
    if input("Would you like to count a particular string? Y/N ").lower() == 'y':
        string_to_count = input("Which string would you like to count? ")

        for i in range(user_int): #loop through the list
            if user_list[i] == string_to_count: #if # at 'i' of list = the string user wants to count
                counter += 1
        return print(user_list, "The string",string_to_count,"appears",counter,"times.")



for i in range (user_int): #randomized the #s inside the list
    user_list.insert(i, randint(1,10))

while True:
    print(user_list)
    
    if input("Exit: Y/N ").lower() == 'y':
        break

    replace_number = int(input("Which number to replace? "))
    number_to_string = input("Replace number with: ")
    
    for i in range(user_int): #loop through the list
        if user_list[i] == replace_number: #if # at 'i' of list = the # user wants to replace
            user_list[i] = number_to_string #replace that # with the user's string


    string_to_count()


    

