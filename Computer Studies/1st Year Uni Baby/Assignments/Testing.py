#101286968
#Nick Dang
#Description: read a source image & create a larger version of that image
# using a pointillist style.

import random
import sys
import pygame


#read image name and load
a = sys.argv[1]
image = pygame.image.load(a)

#get image height & width
(image_width,image_height) = image.get_size()
screenPoints = pygame.display.set_mode((image_width*5, image_height*5)) #upscale drawn image by 5


#put image onto window surface
#screen.blit(image,(0,0))

#check every single pixel of source image
for y in range(image_height):
   for x in range(image_width):
        (r, g, b, _) = image.get_at((x, y)) #check RGB value of pixel
        
        #cacl # of circles for red, green and blue
        a = int(r/60)
        c = int(g/60)
        d = int(b/60)

        if x == 0 and y ==0: #check left corner pixel
            if (r,g, b, _) == (250,45, 208): #check if that pixel is magenta
                a = int(r/40) #draw more blue and red points
                c = int(g/70)
                d = int(b/40)
                while a > 0:
                    pygame.draw.circle(screenPoints, (255,0,0),(random.randint((x*5)-15,x*5),random.randint((y*5)-15,y*5)),1)
                    a -=1
                while c > 0:
                    pygame.draw.circle(screenPoints, (0,255,0),(random.randint((x*5)-15,x*5),random.randint((y*5)-15,y*5)),1)
                    c -=1
                while d > 0:
                    pygame.draw.circle(screenPoints, (0,0,255),(random.randint((x*5)-15,x*5),random.randint((y*5)-15,y*5)),1)
                    d -=1
        else: #otherwise draw as normal 
            while a > 0:
                pygame.draw.circle(screenPoints, (255,0,0),(random.randint((x*5)-15,x*5),random.randint((y*5)-15,y*5)),1)
                a -=1
            while c > 0:
                pygame.draw.circle(screenPoints, (0,255,0),(random.randint((x*5)-15,x*5),random.randint((y*5)-15,y*5)),1)
                c -=1
            while d > 0:
                pygame.draw.circle(screenPoints, (0,0,255),(random.randint((x*5)-15,x*5),random.randint((y*5)-15,y*5)),1)
                d -=1

  

pygame.display.update()# update drawn points onto screen

pygame.image.save(screenPoints,"suqintingDrawing.png") #save image


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()