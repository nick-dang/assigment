#101286968
#Nick Dang
#description: a program that does an inverted colour effect whenever a mouse clicks on region of 
#an user-loaded image

from sys import argv
import pygame



image_name = argv[1] #get image name and load
image = pygame.image.load(image_name)

(image_width,image_height) = image.get_size() #get size of image and window to image's size
screen = pygame.display.set_mode((image_width, image_height))

screen.blit(image, (0,0)) #put image onto screen



exit_flag = False
while not exit_flag:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit_flag = True
    mouse_click = pygame.mouse.get_pressed(3) #get mouse click 
    (x,y) = pygame.mouse.get_pos() #get mouse position
    
    if mouse_click == (1,0,0): #if left mouse is clicked
        
        for i in range (x-20,x+20): #loop through the area around the clicked point
            for j in range (y-20,y+20):
                (r,g,b,_) = image.get_at((i,j)) #get the colour of a pixel in an area around the clicked point
                #invert colours
                q = r-(r*0.725) 
                d = g-(g-0.15)
                f = b-(b*0.20)
                screen.set_at((i,j),(q,d,f)) #change colour of that pixel
                
                

    pygame.display.update()

    