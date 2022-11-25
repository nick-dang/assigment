#nick dang
#101286968
#description: 

import pygame

graph = [[1],[0,2],[1,3,13],[2,4,11],[3,5,6,7,8,9,10],[4],[4],[4],[4],[4],[4],[3,12],[11],[2,14],[13,15,16],[14,17],[14],[15,18,19],[17],[17]]
name = ["Outside","Entrace","Hallway 1","Hallway 2","Hallway 3","Small room #5","Small room #6","Small room #7","Small room #8","Small room #9",
 "Small room #10","Small room #11", "Storage Room of room #11","Hallway 4","Big waiting area","Elevator","Garden","Hallway 5","Big room #18","Big room #19"] 



current_location = "Entrance"

image_1st_floor = pygame.image.load("images.jfif")
image_2st_floor = pygame.image.load("2ST_FLOOR.png")

(image_1st_width,image_1st_height) = image_1st_floor.get_size()
(image_2st_width,image_2st_height) = image_2st_floor.get_size()

screen = pygame.display.set_mode((image_1st_width,image_1st_height))

image_1st_floor.blit(screen,(0,0))



pygame.display.update()