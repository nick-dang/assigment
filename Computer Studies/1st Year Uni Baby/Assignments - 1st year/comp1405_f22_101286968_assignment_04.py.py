#101286968
#Nick Dang
#Description: an expert system that guess the user's selected movie choice from 
# a given list

#animated movie list:
#1. Frozen - super power, princess, 
#2. big hero 6 - >1 main characters, heroes, not princess
#3. Aladdin - princess, don't contain super power and no characters turn into animal
#4. wreck it ralph - video game, adventure, >1 main characters 
#5. beauty and the beast - princess, no super power, main character turn into an animal, has magical objects
#6. princess and the frog - princess, no super power, main character turn into animal, no magical objects
#7. Pinocchio - object going adventure, main character isn't an animal
#8. peter pan - >1 main characters, magic things related 
#9. toy story - objects going adventure, main characters are surrounded by other moving objects, there are humans
#10. cars - objects going adventure, no human characters 
#11. monster incs - no video game character
#12. Up - no magic things related, >1 main characters
#13. nemo - main character(s) are animals, animals going adventure
#14. the incredibles - super power, heroes, >1 main characters

#anime movie list: 
#1. Spirited Away - supernatural event, character get lost in an unknown location 
#2. The Garden of Words - no supernatural event, no fantasy, age difference 
#3. A Silent Voice - no supernatural event, no fantasy, no age differnce
#4. Dragon Ball - no supernatural event, fantasy, searching for something important, no interaction with multiple girls
#5. Weathering With You - supernatural event, romance, not made from tv show, no body-swap
#6. Your Name - supernatural event, not made from tv show, body-swap
#7. Rascal Does Not Dream of a Dreaming Girl - supernatural event, made from tv show
#8. Kizumonogatari - fantasy, no searching for something important
#9. My Neighbor Totoro - supernatural event, no romance, no character getting lost 
#10. Date A Live Movie: Mayuri Judgment - fantasy, searching for something important, interact with other girls

#ask user for instruction
from time import sleep, time


userInstruction = input("Do you need instruction? ").lower()
if userInstruction == "yes":
    print("This is an expert system that guess your movie choice based on "\
    "a movie you chose in a subgenre. The questions asked will be yes-no questions.")
   
#ask for subgenre
subGenre = input("What type of subgenre would you like to choose? (animated or anime) ").lower()

#movie choies for animated and anime
if subGenre == "animated":
    if input("Is it a princess/prince movie? ").lower() == "yes":
        if input("Do any of the main characters possess super power? ") =="yes":
            print("It's Frozen")
        elif input("Does the main character(s) turn into some sort of animal? ").lower() == "yes":
            if input("Are there many magic object?").lower()=="yes":           
                print("It's Beauty and The Beast")
            else:
                print("It's Princess and The Frog")
        else:
            print("It's Aladdin")
    elif input("Are there objects, object-like or animals that go on an adventure? ").lower() == "yes":
        if input("Are there many object-like characters that revolve around the mains? ").lower()=="yes":
            if input("Are there any human characters in the movie? ").lower() == "yes":
                print("It's Toy story")
            else:
                print("It's Cars")
    elif input("There are more than 1 main characters? ").lower() == "yes":
        if input("Are there heroes characters? ").lower() == "yes":
            if input("Some of the characters have super power? ").lower() == "yes":
                print("It's The Incredibles")
            else:
                print("It's Big Hero 6")
        elif input("Are there any magic things related? ").lower()=="yes":
            print("It's Peter Pan")
        else:
            print("It's Up") 
    elif input("Are there video characters? ").lower()=="yes":
        print("It's Wreck It Ralph")
    else:
        print("It's Monster Incs")

elif subGenre =="anime":
    if input("Is there a supernatural event that happened in the story? ").lower()=="yes":
        if input("Is it a romance? ").lower() == "yes":
            if input("Is the movie made from a TV Show series? ").lower() == "yes":
                print("It's Rascal Does Not Dream of a Dreaming Girl")
            elif input("Is there a body-swap event that happaned? ").lower() == "yes":
                print("It's Your Name")
            else:
                print("It's Weathering With You")
        elif input("Does the main character(s) get lost in an unknown location? ").lower() == "yes":
            print("It's Spirited Away")
        else: 
            print("It's My neighbor Totoro")

    elif input("Is the movie fantasy? ").lower() =="yes":
        if input("Are some of the major events that happened related to searching for something important? ").lower()=="yes":
            if input("Does the main character(s) interact with multiple girls in the story? ").lower() == "yes":
                print("It's Date A Live Movie: Mayuri Judgment")
            else:
                print("It's Dragon Ball")
        else:
            print("It's Kizumonogatari")
    elif input("Is there an age difference of 5+ between the main character and the second? ").lower() == "yes":
        print("It's The Garden of Words")
    else:
        print("It's A Silent Voice")
    
        
  