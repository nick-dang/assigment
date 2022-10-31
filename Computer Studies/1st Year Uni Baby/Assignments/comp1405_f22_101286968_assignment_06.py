#101286968
#Nick Dang
#Description: create a board game similar to snake and ladder 
#board game features: "Ladder connection" & "snake connection"

import pygame
import random

#method for rolling 2 6-sided dice 
def die():
    a = random.randint(1,3)
    return a

#method to draw grid
def grid():
    for i in range(8): #loop for x-axis
        for j in range(7): #for y-axis
            squares.append(pygame.draw.rect(screen, (0,0,0), (i*squareWidth, j*squareHeight, squareWidth,squareHeight), width=1))

#window & grid dimension
squareWidth = 80
squareHeight= 80
winWid = 640
winHeight = 560

#set up window for 56 grid
screen = pygame.display.set_mode((winWid, winHeight))

#array for squares
squares = []
grid()

b = 6 #starting square number
d = 55 #value of highest square number on the right corner of the lowest row
e = 5
ply1_x_pos = [squares[6][0]+20, squares[6]]
ply1_y_pos = [squares[6][1]+20, squares[6]]    

direction = True #check status depending on whether the players are moving right (True)/left (false)

while ply1_x_pos [1] != squares[49]: #check if players reach the end of board game
    pygame.time.delay(200)
    screen.fill((255,255,255))

    #loop to draw the board game
    grid()
    
    a = die() #roll dice
    print(a)

    
    
    print(direction)
    if direction == True: #when players moving right
        c = int((squares[d][0] - squares[b][0])/80)

        if a <= c: #check if dice value is < than number of squares left
            if (b+7*a) <= d:
                b += 7*a
                print("b value", b)
                ply1_x_pos = [squares[b][0]+20, squares[b]]
            
        elif a > c: #check if dice value is > # of squares left
            print("c value", c)
            if a != c:
                b += 7*c #update location and move all the way to right side

            
            print(b, d)
            if b == d and a > c: #check if player1 touch the border square
                d -= 2
                
                c = a - c -1 #amount of move left after move up 1 row
                if b != 49:
                    b = (b-1)-7*c

                ply1_y_pos = [squares[b][1]+20, squares[b]] #move up 1 row
                ply1_x_pos = [squares[b][0]+20, squares[b]]
                print("b value", b)
                direction = False


    elif direction == False: #when players move left
        c = int((squares[b][0] - squares[e][0])/80)
        print("c value", c)
        if a <= c: #check if dice value is < than number of squares left
            if (b-7*a) >= e:
                b -= 7*a
                print("b value", b)
                ply1_x_pos = [squares[b][0]+20, squares[b]]
            
        elif a > c:
            print("c value", c)
            b -= 7*c #update location and move all the way to left side
            
            
            print("b & e", b, e)
            if b == e: #check if player1 touch the border square
                e -= 2
                c = a - c -1 #amount of move right after move up 1 row
                b = (b-1)+7*c
                ply1_y_pos = [squares[b][1]+20, squares[b]] #move up 1 row
                ply1_x_pos = [squares[b][0]+20, squares[b]]
                print("b value", b)
                direction = True
   
    pygame.draw.rect(screen, (255,0,0), (ply1_x_pos[0], ply1_y_pos[0], 25, 25))
    
    pygame.display.update()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


