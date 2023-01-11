#nick dang
#101286968
#description: implement bogosort and bozosort


from random import randint

def bogosort(list):
    length = len(list) #get length of list
    for i in range (length): #go through the values of list
        temp_ind = randint(0,length-1) #get random index of list to swap
        temp = list[temp_ind] #store the value of the randomized index of list into a temp variable for later swap

        list[temp_ind] = list[i] #swap the values at the 2 indexes
        list[i] = temp

def check_sort(list):
    length = len(list)
    for i in range(length):
        if i != length-1:
            if list[i] > list[i+1]:
                return False
    return True

def bozosort(list):

    length = len(list) #get length of list
    ran_1st_ind = randint(0,length-1) #get 1st random index
    ran_2n_ind = randint(0,length-1)
    temp_1 = list[ran_1st_ind] #store the values from randomized indexes 
    temp_2 = list[ran_2n_ind]

    list[ran_1st_ind] = temp_2 #swap the 2 values
    list[ran_2n_ind] = temp_1
    
def main():
    list =[1,2,3,5,4,6,7] #testing list
    bozosort(list) #swap 2 random values first
    while check_sort(list) == False:
        bozosort(list)
    print(list)

    bogosort(list) #shuffle the tesing list first
    while check_sort(list) == False: #check if shuffle list is sorted
       
        bogosort(list) #shuffle again
    print(list)   
    
    





main()