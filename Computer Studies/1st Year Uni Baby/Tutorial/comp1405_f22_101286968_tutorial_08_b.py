#nick dang
#101286968
#description: read and render a tile map that's specified by the user. Program needs to handle any exception that might appear. 
#tile image assumed to be desert
import pygame


image = pygame.image.load("tutorial_file_desert_0.gif") #load image
(img_wid,img_hei) = image.get_size() #get image size


while True:
    file_name = input("File name: ") #ask user for file name
    try:
        file = open(file_name,"r") #open file
        line = file.readline() #read first line to get specified tile name

        if 'desert' not in line: #quit if the specified tile in file doesn't exist
            quit()
        
        file.close() #close file
        break
    except FileNotFoundError: #catch error of file not found
        print("File not found")
    except: #catch other error that might occur
        print("error")
        

#blit image with correct dimensions
screen = pygame.display.set_mode((img_wid,img_hei))  
screen.blit(image,(0,0)) 
    
pygame.display.update()
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()