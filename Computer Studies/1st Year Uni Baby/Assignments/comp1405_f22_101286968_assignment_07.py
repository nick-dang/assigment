#101286968
#Nick Dang
#description: a program that does an inverted colour effect whenever a mouse clicks on region of 
#an user-loaded image

from sys import argv
from turtle import screensize
import pygame



a = argv[1] #get image name and load
image = pygame.image.load(a)

(image_width,image_height) = image.get_size() #get size of image and window to image's size
screen = pygame.display.set_mode((image_width, image_height))


screen.blit(image, (0,0))


mouse_click = pygame.mouse.get_pressed(1)

print(mouse_click)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()