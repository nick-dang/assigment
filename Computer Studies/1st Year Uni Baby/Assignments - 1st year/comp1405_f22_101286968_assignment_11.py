#nick dang
#101286968
#description: do a scroll-like end credit


import pygame
from time import sleep
pygame.init()
#create a try catch for when program can't find the resume-restart file, then it will ask user to enter name of the file that contains the credit paragraph then display.
#if window's closed, create a file and stored the last line that was displayed. 

win_width = 1000 #window size
win_height = 500
screen = pygame.display.set_mode((win_width,win_height))
font = pygame.font.SysFont('arial',20,italic=True,bold=True) #set font and size
line_list = [] #store lines in a list
x_pos_let = 0 #pos for text location on the window 
y_pos_let = 0

try:  #try to read the resume-restart file
    file = open("saved File.txt",'r')
except FileNotFoundError: #if not found, then ask user for file name that has the credit to display
    #file_name = input("Enter file name: ") #ask for file name
    file = open("end_credits.txt",'r') #open the file

    while True: #loop to put lines into a list
        line = file.readline() #read line
        
        if not line: #break when there's nothing else to read
            break
        line_list.append(line) #put the read lines into a list 
    
    for i in range(len(line_list)): #go through the length of the line list
        for j in range(len(line_list[i])): #go through every letter of a phrase to display one at a time
            text = font.render(line_list[i][j],True,(255,255,255)) #render the font 

            screen.blit(text,(x_pos_let,y_pos_let)) #blit the texts onto window

            pygame.display.update()
            sleep(.05)
            
            x_pos_let += 11 #update individual letter's x pos
            
            if x_pos_let > (win_width -300): #go down 1 line if text touches border of window 
                if line_list[i][j] == ' ': #check if there's a space at the current 'letter' pos
                    x_pos_let = 0 #reset texts pos
                    y_pos_let = y_pos_let + 18
            

exit_flag = False
while not exit_flag:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit_flag = True
            print("hello")



