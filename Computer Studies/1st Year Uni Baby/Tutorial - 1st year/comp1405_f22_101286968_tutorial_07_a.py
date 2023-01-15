#nick dang
#101286968
#description: a program that has a function to check if a matrix is valid matrix or 
# not based 3 properties - every row is a list, every row is the same length, every element is numeric


def check_matrix(matrix):
    list_to_check_matrix = [] #a list to keep track that every requirement of "valid matrix" is met
    
    for row in matrix: #check every row in that matrix is a list
        if isinstance(row,list) == True:
            list_to_check_matrix.append(True)
            
        else:
            list_to_check_matrix.append(False)

    next_row = 0
    for row in range(len(matrix)): #check every row is the length
        next_row = row +1
        if next_row >= len(matrix): #check if next row is out of index of list 
            break 
        
        if len(matrix[row]) == len(matrix[next_row]): #check if current row and next row is same length
            list_to_check_matrix.append(True) 
        
        else:
            list_to_check_matrix.append(False)
    
    for row in range(len(matrix)): #check every element in the matrix is numeric
        for val in matrix[row]:
            if isinstance(val,int) == True or isinstance(val,float) == True:
                list_to_check_matrix.append(True)
            else:
                list_to_check_matrix.append(False)

    if False in list_to_check_matrix:
        return False
    else:
        return True #meaning matrix isn't valid
        

if check_matrix([[1,2,3],[4,5,6]]) == True:
    print("hello")