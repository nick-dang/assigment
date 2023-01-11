# 101286968
# Nick Dang
# Description: a simple menu that's inspired by the "General Store"
# in "The Oregon Trail". It allows user to select profession with a starting balance
# and they can specific how much supplies they want to buy.

print("WELCOME TO TORONTO TRAIL\n")

# ask user for profession
choicePro = int(input(
    "You may:\n1.Be a banker from Ottawa\n2.Be a carpenter from Manitoba\n3.Be a farmer from Albeta\nWhat is your choice? "))
if choicePro == 1:
	money = 1600
	print("You are currently a banker with $", money, "\n")
elif choicePro == 2:
	money = 800
	print("You are currently a carpenter with $", money, "\n")
elif choicePro == 3:
	money = 600
	print("You are currently a farmer with $", money, "\n")

# initialized amount for ox, food, ammo
amountOx = 0
amountFood = 0
amountAmmo = 0

# ask user for item to buy
choiceItem = int(input("What items do you want to buy?\n1.Ox - $40 per\n2.Food - $0.20 per\n3.Box of Ammo - $2.00 per\n"))

# check what item user picked
if choiceItem == 1:
       amountOx = int(input("How much? "))  # ask amount
       total = amountOx*40
       money -= total
       
elif choiceItem== 2:
       amountFood= int(input("How much? "))
       total= amountFood*0.2
       money-= total
       
elif choiceItem== 3:
       amountAmmo= int(input("How much? "))
       total= amountAmmo*2
       money-= total
       
#print user's amount of money left
print("\nYou currently have " + chr(36) + "{:.2f}".format(money), "\nYou have ", amountOx, " Ox, ", amountFood, " pounds of food,",amountAmmo, "boxes of ammo.") 







	


