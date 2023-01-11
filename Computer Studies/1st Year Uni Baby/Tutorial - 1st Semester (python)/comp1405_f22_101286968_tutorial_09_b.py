#nick dang
#101286968
#description: do Empirical Performance Analysis for bogosort and bozosort

from random import randint
from time import time

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
    max_problem_size = 50 #max problem size
    starting_problem_size = 10
    increase_list_size_by = 10
    
    num_of_trial = 30
    timing_bogosort = 0
    timing_bozosort = 0

    for size in range(starting_problem_size,max_problem_size,increase_list_size_by): #the problem size increases by 10 after every 30 trials. 
        for j in range(num_of_trial): 
            rand_list = [ randint(0, 10) for i in range(size) ] #generate random list 
            rand_list_bogosort = rand_list #store the lists for sorting 
            rand_list_bozosort = rand_list

            start_time = time()
            while check_sort(rand_list_bogosort) == False: #check if the list's sorted
                bozosort(rand_list_bogosort) #sort again
            stop_time = time()
            timing_bogosort += stop_time - start_time #get time


            start_time = time()
            while check_sort(rand_list_bozosort) == False:
                bozosort(rand_list_bozosort)
            stop_time = time()
            timing_bozosort += stop_time - start_time
            

        timing_bogosort /= num_of_trial #get average time per trial with a particular size
        timing_bozosort /= num_of_trial

        print("For size",size,"bogosort took: ",timing_bogosort)
        print("For size",size,"bozosort took: ",timing_bozosort)
        
    
    
    

main()