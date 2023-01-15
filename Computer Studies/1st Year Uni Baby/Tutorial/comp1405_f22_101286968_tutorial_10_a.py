#nick dang
#101286968
#description: 2 functions for checking if a list of numbers have an odd then add 10 to it.
#1 function done non-recursively and 1 recursive





def first_func(list):

    for i in range(len(list)):
        if (list[i]%2) == 1:
            list[i] += 10
            
    return list

def second_func(list):
    a = 0 
    b = 1
    if list == []:
        return list 
    else:
        #simplify 
        
         #store the 1st value of the list into a variable for later checking if it's odd or even
        simplified = list[a]
        print(simplified)
        
        
        

    return list


list = [1,2,3]
second_func(list)
