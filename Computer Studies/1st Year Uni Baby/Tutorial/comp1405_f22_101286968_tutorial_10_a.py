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
    if (list[0]%2) == 1:
        list[0] += 10
    else:
        #simplify 
        
        simplified = list[1:]

    return list

print(first_func([1,2,3]))