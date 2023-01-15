#Nick Dang
#101286968
#a simple drawing of a person balancing a ball on finger
import pygame

#display
screen = pygame.display.set_mode((500,500))
screen.fill(color=(255,255,255))

#draw head
pygame.draw.circle(screen,(0,0,0),(250,200),40,width=5)

#draw body
pygame.draw.polygon(screen,(0,0,0),((225,250),(275,250),(295,290),(295,350),(205,350),(205,290)))

#draw arms
pygame.draw.arc(screen,(0,0,0),(120,100,170,170),3.142,4.712,width=3)
pygame.draw.arc(screen,(0,0,0),(215,270,170,170),6.283,1.571,width=3)

#draw ball
pygame.draw.circle(screen,(225,127,39),(120,148),40,width=3)
pygame.draw.arc(screen,(225,127,39),(95,100,100,100),2.154,3.926,width=3)
pygame.draw.arc(screen,(225,127,39),(115,100,100,100),2.312,3.926,width=3)

#draw legs
pygame.draw.arc(screen,(32,32,32),(150,360,170,170),1.571,3.141,width=3)
pygame.draw.arc(screen,(32,32,32),(270,275,170,170),3.141,4.712,width=3)

#draw eyes
pygame.draw.circle(screen,(0,0,0),(227,200),10,width=3)
pygame.draw.circle(screen,(0,0,0),(267,200),10,width=3)
pygame.draw.circle(screen,(0,0,0),(225,199),5,width=0)
pygame.draw.circle(screen,(0,0,0),(265,199),5,width=0)

pygame.display.flip()
pygame.time.delay(3000)