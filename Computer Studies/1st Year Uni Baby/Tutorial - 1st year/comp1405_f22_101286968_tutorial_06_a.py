#101286968
#nick dang
#description: ask user to add a number to list, remove the last value of the list or exit in a loop. after exit print the len of list without using len()

user_list = [] #user's list
counter = 0 #keep count when list has been added/removed

while True:
    user = input("Would you like to add a number to list? Type 'add'\n"
                "Remove the last number of the list: Type 'rem'\n"
                "Exit: Type 'exit'\n")
    
    if user.lower() == 'exit': #exit 
        break
    elif user.lower() == 'add': #add value to list
        counter +=1
        if input("Add to the of list or Insert: Type 'add' or 'insert'").lower() == 'add':
            user_list.append(int(input("Add a number: ")))
        else:
            value = int(input("Please add a value of: "))
            pos_of_value = int(input("Please add a position to add the value: "))
            user_list.insert(pos_of_value,value)
    
    elif user.lower() == 'rem': #remove last value from list
        user_list.pop() 
        counter -=1

print(user_list, "len is",counter)