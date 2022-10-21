#Nick Dang
#101286968
#recreation of Hilma af klint's "Svanen"

import pygame

#display a window
screen = pygame.display.set_mode((500,500))

#change surface colour
screen.fill(color=(180,71,48))

#draw white semi-circle
pygame.draw.arc(screen,(224,215,208),(100,100,300,300),1.571,4.712,width=60)

#draw blue semi-circle
pygame.draw.arc(screen,(71,124,174),(100,100,300,300),4.712,1.571,width=60)

#draw black circle
pygame.draw.circle(screen, (32,32,32), (250, 250), 100, 0)

#draw yellow semi-circle
pygame.draw.arc(screen,(225, 182,87), (150,150,200,200),4.712,1.571,width=60)

#draw pink circle
pygame.draw.circle(screen, (220,143,127), (250, 250), 50, 0,draw_top_right=True, 
draw_top_left=False, draw_bottom_left=False, draw_bottom_right=True)


pygame.display.flip()
pygame.time.delay(2000)

