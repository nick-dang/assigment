<<<<<<< HEAD:Computer Studies/1st Year Uni Baby/Assignments/testing.py


list = [1,2,3,4,5]



print(list[len(list)//2:])

=======
a = "Hello, are you new here? Well, let me introduce you to my program. My name is fdjsalk. Nice to meet you.  "

import time
import pygame
pygame.init()
exit_flag = False
win_width = 1000
win_height = 500
screen = pygame.display.set_mode((win_width,win_height))
font = pygame.font.SysFont('arial',20,italic=True,bold=False)
c = 7
b = 0
for i in a:
    
    text = font.render(i,True,(255,255,255))

    screen.blit(text,(c,b))

    pygame.display.update()
    #print(i, end='',flush=True)
    time.sleep(0.05)
    c += 11
    if c > (win_width -300): #go down 1 line if text touches border of window
        if i == ' ':
            c = 0
            b = 18



            
while not exit_flag:
    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit_flag = True
    


    
>>>>>>> e79523e4fdf2bc60ce7c9bf5d25c312ddcdb20b6:Computer Studies/1st Year Uni Baby/Assignments - 1st Semester (python)/testing.py
