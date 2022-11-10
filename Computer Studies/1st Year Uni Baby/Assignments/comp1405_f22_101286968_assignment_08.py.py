#101286968
#nick dang
#description: a program that designs a set of cartoon eyes, cartoon mouth and cartoon hat

import pygame


def draw_eyes():
    """ pygame.draw.circle(win_sfc, (0,0,0), (115,225), 20,width=1)
    pygame.draw.circle(win_sfc, (0,0,0), (210,225), 20,width=1) """
    pygame.draw.ellipse(win_sfc,(0,0,0), (95,200, 50, 70), width=1)
    pygame.draw.ellipse(win_sfc,(0,0,0), (95,200,45,50), width=1)
win_sfc = pygame.display.set_mode((500,500))

win_sfc.fill((255,255,255))


draw_eyes()
pygame.draw.circle(win_sfc, (0,0,0), (150,250), 100, width=1)








pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()