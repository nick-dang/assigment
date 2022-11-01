#101286968
#Nick Dang
#Description: create a board game similar to snake and ladder 
#board game features: "Ladder connection" & "snake connection"

import pygame
import random

#method for rolling 2 6-sided dice 
def die():
    diceValue = random.randint(1,8)
    return diceValue

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

player1CurrentPos = 6 #player 1 starting square
player1End = 55 #value of highest square number on the right corner of the lowest row
player1LeftColumn = 5 #value of lowest square number on the left corner of the 2nd lowest row
ply1_x_pos = [squares[6][0]+20, squares[6]] #x & y positions for player 1
ply1_y_pos = [squares[6][1]+20, squares[6]]    

player2CurrentPos = 6 #player 2 starting square
player2End = 55 #value of highest square number on the right corner of the lowest row
player2LeftColumn = 5 #value of lowest square number on the left corner of the 2nd lowest row
ply2_x_pos = [squares[6][0]+40, squares[6]] #x & y positions for player 2
ply2_y_pos = [squares[6][1]+40, squares[6]]    

player1Direction = True #check status depending on whether the players are moving right (True)/left (false)
player2Direction = True
playerTurn = True #switch between players, player 1 (True) & player 2 (false)

while ply1_x_pos [1] != squares[49] or ply2_x_pos [1] != squares[49]: #check if players reach the end of board game
    pygame.time.delay(500)
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255,0,0), (ply1_x_pos[0], ply1_y_pos[0], 25, 25))
    pygame.draw.rect(screen, (0,255,0), (ply2_x_pos[0], ply2_y_pos[0], 25, 25))
    #loop to draw the board game
    grid()
    
    
    #player 1 move
    if playerTurn == True: 
        diceValue = die() #roll dice
        print(diceValue)
        print(player1Direction)

        if player1Direction == True: #when players moving right
            player1SquaresLeft = int((squares[player1End][0] - squares[player1CurrentPos][0])/80)
            
            if ply1_x_pos[1] == squares[20]:
                player1CurrentPos = 32
                ply1_x_pos = [squares[player1CurrentPos][0]+20, squares[player1CurrentPos]]


            if ply1_x_pos[0] in range(0, 560) and ply1_y_pos[0] == 20 and (player1CurrentPos +7*diceValue)  > 49: #check that current position will have to roll the exact squares left to land on the finish line
                
                playerTurn = False
            elif diceValue <= player1SquaresLeft: #check if dice value is < than number of squares left
                
                if (player1CurrentPos+7*diceValue) <= player1End: #check if current position will move out of bound if move to the dice value 
                    player1CurrentPos += 7*diceValue#move the current position to the dice value 
                    print("player1 current pos", player1CurrentPos)
                    ply1_x_pos = [squares[player1CurrentPos][0]+20, squares[player1CurrentPos]] #move player 1
                    playerTurn = False #switch player
            
            elif diceValue> player1SquaresLeft: #check if dice value is > # of squares left
                
                print("ply1 SquaresLeft", player1SquaresLeft)
                player1CurrentPos += 7*player1SquaresLeft #update location and move all the way to right side
                playerTurn = False

                print(player1CurrentPos, player1End)
                if player1CurrentPos == player1End: #check if player1 touch the border square
                    player1End -= 2
                    
                    player1SquaresLeft = diceValue- player1SquaresLeft -1 #amount of move left after move up 1 row

                    if player1CurrentPos != 49: #check if current position doesn't equal to 49 (the last square)
                        player1CurrentPos = (player1CurrentPos-1)-7*player1SquaresLeft

                    ply1_y_pos = [squares[player1CurrentPos][1]+20, squares[player1CurrentPos]] #move up 1 row
                    ply1_x_pos = [squares[player1CurrentPos][0]+20, squares[player1CurrentPos]]
                    playerTurn = False
                    print("player1 current pos", player1CurrentPos)
                    player1Direction = False

        elif player1Direction == False: #when player 1 move left
            player1SquaresLeft = int((squares[player1CurrentPos][0] - squares[player1LeftColumn][0])/80)
            print("ply1 SquaresLeft", player1SquaresLeft)
            if diceValue<= player1SquaresLeft: #check if dice value is < than number of squares left
                if (player1CurrentPos-7*diceValue) >= player1LeftColumn:
                    player1CurrentPos -= 7*diceValue
                    print("player1 current pos", player1CurrentPos)
                    ply1_x_pos = [squares[player1CurrentPos][0]+20, squares[player1CurrentPos]]
                    playerTurn = False
                
            elif diceValue> player1SquaresLeft:
                print("ply1 SquaresLeft", player1SquaresLeft)
                player1CurrentPos -= 7*player1SquaresLeft #update location and move all the way to left side
                playerTurn = False
                
                print("ply1CurrentPos & ply1LeftColumn", player1CurrentPos, player1LeftColumn)
                
                if player1CurrentPos == player1LeftColumn: #check if player1 touch the border square
                    player1LeftColumn -= 2
                    player1SquaresLeft = diceValue- player1SquaresLeft -1 #amount of move right after move up 1 row
                    
                    player1CurrentPos = (player1CurrentPos-1)+7*player1SquaresLeft

                    

                    ply1_y_pos = [squares[player1CurrentPos][1]+20, squares[player1CurrentPos]] #move up 1 row
                    ply1_x_pos = [squares[player1CurrentPos][0]+20, squares[player1CurrentPos]]
                    playerTurn = False
                    print("player1 current pos", player1CurrentPos)
                    player1Direction = True
        
    #player 2 move
    if playerTurn == False: 
        diceValue = die() #roll dice
        print(diceValue)
        print(player2Direction)

        if player2Direction == True: #when players moving right
            player2SquareLeft = int((squares[player2End][0] - squares[player2CurrentPos][0])/80)
            
            if ply2_x_pos[0] in range(0, 560) and ply2_y_pos[0] == 40 and (player2CurrentPos+7*diceValue)  > 49: #check that current position will have to roll the exact squares left to land on the finish line
                
                playerTurn = True
            elif diceValue<= player2SquareLeft: #check if dice value is < than number of squares left
                if (player2CurrentPos+7*diceValue) <= player2End: #check if current position will move out of bound if move to the dice value 
                    player2CurrentPos += 7*diceValue#move the current position to the dice value 
                    print("player2 current pos", player2CurrentPos)
                    ply2_x_pos = [squares[player2CurrentPos][0]+40, squares[player2CurrentPos]] #move player 1
                    playerTurn = True
            
            elif diceValue > player2SquareLeft: #check if dice value is > # of squares left
                print("player2 squaresLeft", player2SquareLeft)
                player2CurrentPos += 7*player2SquareLeft #update location and move all the way to right side
                
                print(player2CurrentPos, player2End)

                if player2CurrentPos == player2End: #check if player1 touch the border square
                    player2End -= 2
                    
                    player2SquareLeft = diceValue- player2SquareLeft -1 #amount of move left after move up 1 row
                    if player2CurrentPos != 49: #check if current position doesn't equal to 49 (the last square)
                        player2CurrentPos = (player2CurrentPos-1)-7*player2SquareLeft

                    ply2_y_pos = [squares[player2CurrentPos][1]+40, squares[player2CurrentPos]] #move up 1 row
                    ply2_x_pos = [squares[player2CurrentPos][0]+40, squares[player2CurrentPos]]
                    playerTurn = True
                    print("player2 current pos", player2CurrentPos)
                    player2Direction = False


        elif player2Direction == False: #when player 2 move left
            player2SquareLeft = int((squares[player2CurrentPos][0] - squares[player2LeftColumn][0])/80)
            print("player2 squaresLeft", player2SquareLeft)
            if diceValue<= player2SquareLeft: #check if dice value is < than number of squares left
                if (player2CurrentPos-7*diceValue) >= player2LeftColumn:
                    player2CurrentPos -= 7*diceValue
                    print("player2 current pos", player2CurrentPos)
                    ply2_x_pos = [squares[player2CurrentPos][0]+40, squares[player2CurrentPos]]
                    playerTurn = True

            elif diceValue > player2SquareLeft:
                print("player2 squaresLeft", player2SquareLeft)
                player2CurrentPos -= 7*player2SquareLeft #update location and move all the way to left side

                
                print("ply2Pos & ply2LeftColumn", player2CurrentPos, player2LeftColumn)
                if player2CurrentPos == player2LeftColumn: #check if player1 touch the border square
                    player2LeftColumn -= 2 #subtract left border by 2

                    player2SquareLeft = diceValue- player2SquareLeft -1 #amount of move right after move up 1 row
                    player2CurrentPos = (player2CurrentPos-1)+7*player2SquareLeft
                    ply2_y_pos = [squares[player2CurrentPos][1]+40, squares[player2CurrentPos]] #move up 1 row
                    ply2_x_pos = [squares[player2CurrentPos][0]+40, squares[player2CurrentPos]]
                    playerTurn = True
                    print("player2 current pos", player2CurrentPos)
                    player2Direction = True



   
    
    pygame.display.update()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

