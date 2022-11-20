#nick dang
#101286968
#description: adding 2 matrices together


def add_matrix(matrix_1,matrix_2):
    result_matrix = []
    #check if 2 matrices have the same amount of rows and columns
    if (len(matrix_1) == len(matrix_2)) and (len(matrix_1[0]) == len(matrix_2[0])):
        print("same dim")
        for row in range(len(matrix_1)): #loop through the row 
            result_row = []
            for val in range(len(matrix_1[0])): #location of column
                result_row.append(matrix_1[row][val] + matrix_2[row][val]) #add each from each column 
            result_matrix.append(result_row) #add sum of matrix of a row to a new matrix
        
        print(result_matrix)
    else: #return empty list of 2 matrices
        return matrix_1.clear(), matrix_2.clear()


