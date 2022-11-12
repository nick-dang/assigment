#101286968
#nick dang
#description: a program that designs a set of cartoon eyes, cartoon mouth and cartoon hat

import pygame

#method to draw eyes
def draw_eyes():
    #pygame.draw.ellipse(win_sfc,(0,0,0), (95,200, 50, 70), width=1) #eye
    pygame.draw.ellipse(win_sfc,(0,0,0), (97,200,45,50),width=1) # first eye
    pygame.draw.arc(win_sfc, (0,0,0), (100,210,40,10), 3.14, 6.21) #eyelid
    pygame.draw.arc(win_sfc, (0,0,0), (104,210,30,20), 3.14, 6.21,width=5) #black part of eye
    pygame.draw.arc(win_sfc, (0,0,0), (100,240,40,15), 3.14, 6.21,) #black part of eye
    pygame.draw.arc(win_sfc, (0,0,0), (103,250,35,10), 3.14, 6.21,) #black part of eye

    pygame.draw.ellipse(win_sfc,(0,0,0), (160,200,45,50),width=1) # 2nd eye
    pygame.draw.arc(win_sfc, (0,0,0), (160,220,44,10), 3.14, 6.21) #eyelid
    pygame.draw.arc(win_sfc, (0,0,0), (167,220,30,20), 3.14, 6.21,width=5) #black part of eye
    pygame.draw.arc(win_sfc, (0,0,0), (160,240,40,15), 3.14, 6.21,) #black part of eye
    pygame.draw.arc(win_sfc, (0,0,0), (163,250,35,10), 3.14, 6.21,) #black part of eye
    pygame.draw.arc(win_sfc, (0,0,0), (163,255,35,10), 3.14, 6.21,) #black part of eye

#method to draw hat 
def draw_hat():
    pygame.draw.arc(win_sfc,(185,122,87), (200,180,100,150),0,3.14,width=50) #draw the curve part of hat

    pygame.draw.polygon(win_sfc,(129,81,54),[(130,250),(160,280),(340,280),(370,250)]) #draw bottom part of hat

    pygame.draw.lines(win_sfc,(255,242,0),True,[(250,200),(230,250),(270,220),(230,220),(270,250)],width=2) #draw star
    
    return print("This is a cowboy hat!")

#method to draw mouth
def draw_mouth(x,y):
    pygame.draw.arc(win_sfc,(0,0,0),(x,y,100,100),3.50,6) #line of mouth
    pygame.draw.arc(win_sfc,(0,0,0),(x,y-80,100,220),3.50,6) #2nd line of mouth

    pygame.draw.arc(win_sfc,(255,0,0),(x+35,y+130,35,35),0.75,2.5,width=8) #tongue

    pygame.draw.line(win_sfc,(0,0,0),(x+7,y+63), (x-3,y+73)) #smirk
    pygame.draw.line(win_sfc,(0,0,0),(x+93,y+58), (x+103,y+68)) #smirk
    pygame.draw.lines(win_sfc,(0,0,0),False, [(x+35,y+97),(x+35,y+125),(x+65,y+125),(x+65,y+97)]) #teeth
    pygame.draw.line(win_sfc,(0,0,0),(x+50,y+99),(x+50,y+125)) #line between teeth
    
