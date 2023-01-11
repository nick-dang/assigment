#Nick Dang
#101286968

import pygame

#display a window
screen = pygame.display.set_mode((480,640))

#change surface color 
screen.fill(color = (255,255,255))

#draw purple polygon
pygame.draw.polygon(screen, (131,117,175), [(80,106),(0,214),(80,319),(160,319),(160,213),(80,213)])

#draw orange polygon
pygame.draw.polygon(screen, (200,107,54), [(80,0),(160,106),(320,106),(400,213),(400,106),(320,0)])

#update screen
pygame.display.flip()

#save image
pygame.image.save(screen, "assigned_image_for_101286968.png")

#put time delay on how long window's opened 
pygame.time.delay(5000)