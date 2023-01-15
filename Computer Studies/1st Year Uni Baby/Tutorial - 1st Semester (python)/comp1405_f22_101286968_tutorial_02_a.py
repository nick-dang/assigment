#Nick Dang
#101286968
#Description: calculate user's age, with consideration whether they were
#born on leap day or not.

name= input("Your name ")
currentYear= int(input("The current year "))
userYear = int(input("The year you were born "))
leapYear= input("Were you born on leap day? ")

if (leapYear=="Y".lower()):
	ageLeap=(currentYear-userYear)/4
	print("Name: ",name,"\nAge in Leap Year: ",int(ageLeap))
else:
	final= currentYear-userYear
	print("Name: ",name,"\nAge: ",final)