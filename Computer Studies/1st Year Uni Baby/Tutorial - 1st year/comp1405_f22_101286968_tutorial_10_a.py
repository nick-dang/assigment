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
    if list == []: #simply solution is when the list has nothing and return an empty list
        result = []
        
    else:
        simplified = list[1:] #slice the list 

        recursive = second_func(simplified) #recursive call 
        result = recursive
        if list[0] % 2 == 1: #check if value is odd then add 10
            result.insert(0,list[0] + 10) 
        else:
            result.insert(0, list[0]) 
    return result


list = [3,65,2,3,4]

print(second_func(list))


