#nick dang
#101286968
#description: ask user to name an tile map file that has the width and height requested. Then write that file. 

from random import randint



file_name = input("Name of file: ") 
prefix = input("Prefix: ")
file = open(file_name, "w")


list = []

#size of map
row = int(input("width: ")) 
column = int(input("height: ")) 

#generate map from user's inputs
for i in range(row): 
    list.append([])
    for j in range(column): #generate random numbers in each row
        list[i].insert(j,randint(0,3))

run = True
while run: #write the map into file
    file.write("tiles: " + prefix+"\n")

    for i in range(len(list)):
        for val in list[i]:
            file.write(str(val)+',')
        file.write("\n")

    run = False
    

