#nick dang
#101286968
#description: a simple text adventure game. Can go around the map to collect items and switch between 1st and 2nd floor when step into elevator. 

import pygame
from random import shuffle

graph = [[1],[0,2],[1,3,13],[2,4,11],[3,5,6,7,8,9,10],[4],[4],[4],[4],[4],[4],[3,12],[11],[2,14],[13,15,16],[14],[14],[18],[17,19,20],[18],[18]]
name = ["outside","entrance","hallway 1","hallway 2","hallway 3","small room #5","small room #6","small room #7","small room #8","small room #9",
 "small room #10","small room #11", "storage room of room #11","hallway 4","waiting area","1st floor elevator","garden","2nd floor elevator","hallway 5","room #19","room #20"] 

#description for each area
descrip = ["This area is a bit dark... might want to go back inside.", "This is the entrance. It feels rather quiet here.","This is the first hallway."
,"There's nothing special here.","There are a lot of rooms here.","This room is really messy.","This room looks nice and clean.","The atmostphere in this room feels strange.",
"Nothing special here.","This could be a nice place to stay.","This is a small room.","This room has a storage room.","The light in this storage room is broken.","This hallway is leading to a place somewhere.",
"This is a very big waiting area.","","The grass here looks very long.","","This hallway is a deadend.","This room is bigger than the previous ones.","This must be the biggest room in this building."]

#direction for area
dir_of_room = [["north"],["south","north"],["south","west","east"],["east","west","north"],["east","south","north"],["north"],["north"],["north"],["south"],["south"],["south"],["south","north"],["south"],["west","east"],
["west","east","south"],["west"],["north"],["west"],["east","south","north"],["north"],["south"]]

#create items and randomize for each area
item = ["","","","","business card","","key","","","phone","flower","sandwich","","","","","","","","","",]
shuffle(item)
user_inv = [] #user's inventory

curr_loc = "entrance"


image_1st_floor = pygame.image.load("1ST_FLOOR.png") #get images for 2 floors
image_2nd_floor = pygame.image.load("2ND_FLOOR.png")

(image_1st_width,image_1st_height) = image_1st_floor.get_size() #get sizes
(image_2nd_width,image_2nd_height) = image_2nd_floor.get_size()
screen = pygame.display.set_mode((image_1st_width,image_1st_height))
screen.blit(image_1st_floor,(0,0))

pygame.display.update()


while True:
    
    indx_loc = name.index(curr_loc) #get index of the current location
    print("Your current location is: ",curr_loc)
    print(descrip[indx_loc]) #print the description of each area
    print()

    if curr_loc != name[0] or curr_loc != name[15] or curr_loc != name[17]: #dont assign an item into 'outside' and 'elevator'
        if item[indx_loc] != "": #check if the item in the index of current location isn't an empty string
            print("This room contains: ",item[indx_loc]) #then display the item if there's one
            if input("Do you want to take this item?: ").lower() == 'take': #ask user if they want to take item
                user_inv.append(item[indx_loc]) #add that item into user's inventory list
                item[indx_loc] = ""
    
    print("From your current location, you could go to: ")
    for i in graph[indx_loc]: #a loop to print the different exits available        
        print("\t", name[i]) #print the exits
            
        
    if curr_loc == name[4]: #the rooms in hallway 3 is an exception of not needing to use 'north/south/east/west to navigate 
        print("Can enter any room without typing 'north/south/east/west', except the hallway.")
    next_loc = input("Where do you want to go?: ")

    if next_loc.lower() != 'inventory': #check if user's input isn't inventory 
        if curr_loc == name[4]: #checking if user is at hallway 3
            #checks if user's typing term to navigate 
            if (next_loc != name[5] and next_loc != name[6] and next_loc != name[7] and next_loc != name[8] and next_loc != name[9] and next_loc != name[10]) and (next_loc != "east"):
                print("There's no such room.")
            elif next_loc == "east": #if user wants to exit hallway 3
                curr_loc = name[3]
            else: #otherwise user's input for the small rooms equal to current location
                curr_loc = next_loc

        elif next_loc == 'quit': #break out of loop if user types 'quit'
            break        

        elif next_loc not in dir_of_room[indx_loc]: #check if user's typing the correct input 
            print("You can't go this way.")
        
        elif next_loc in dir_of_room[indx_loc]: #otherwise move user's location
            direction = dir_of_room[indx_loc].index(next_loc) #get the index of the direction of the room
            curr_loc = name[graph[indx_loc][direction]] #update user's location

            if curr_loc == name[15]: #switch between floor due to elevator
                screen = pygame.display.set_mode((image_2nd_width,image_2nd_height)) #switch window size and floor map
                screen.blit(image_2nd_floor,(0,0))
                curr_loc = name[18]
            elif curr_loc == name[17]:
                screen = pygame.display.set_mode((image_1st_width,image_1st_height)) #switch window size and floor map
                screen.blit(image_1st_floor,(0,0))
                curr_loc = name[14]
        
        print()
    elif next_loc == 'inventory': #if user's input is inventory
        #display every item in user's inventory
        print("Inventory:", ", ".join(user_inv))
        print()
    
    pygame.display.update()
    
    

    

    
    

    



