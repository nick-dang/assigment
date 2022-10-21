#101286968
#Nick Dang
#Description: user enters numerical grades for tutorials, quizzes, assignments
# and exams and return a final letter grade.

#prompt user f and  final grades in 4 categories
gradeTut= int(input("Enter your final grade for tutorial: "))
gradeQuizz= int(input("Enter your final grade for quizz: "))
gradeAssign= int(input("Enter your final grade for assignment: "))
gradeExam= int(input("Enter your final grade for exam: "))

#get %grade from each of them
finalTut= gradeTut*(1/10)
finalQuizz= gradeQuizz*(3/10)
finalAssign= gradeAssign*(2/5)
finalExam= gradeExam*(1/5)

#add them together
finalGrade= finalTut+finalQuizz+finalAssign+finalExam

#check the final numerical grade
if(finalGrade >= 0 and finalGrade < 50):
	letterGrade= "F"
elif(finalGrade >= 50 and finalGrade < 53):
	letterGrade= "D-"
elif(finalGrade >= 53  and  finalGrade < 57):
	letterGrade= "D"
elif(finalGrade >= 57  and  finalGrade < 60):
	letterGrade= "D+"
elif(finalGrade >= 60  and  finalGrade < 63):
	letterGrade= "C-"
elif(finalGrade >= 63  and  finalGrade < 67):
	letterGrade= "C"
elif(finalGrade >= 67  and  finalGrade < 70):
	letterGrade= "C+"
elif(finalGrade >= 70  and  finalGrade < 73):
	letterGrade="B-"
elif(finalGrade >= 73  and  finalGrade < 77):
	letterGrade= "B"
elif(finalGrade >= 77  and  finalGrade < 80):
	letterGrade= "B+"
elif(finalGrade >= 80  and  finalGrade < 85):
	letterGrade= "A-"
elif(finalGrade >= 85  and  finalGrade < 90):
	letterGrade= "A"
elif(finalGrade >= 90  and  finalGrade < 100):
	letterGrade= "A+"

print("Your final grade is ", letterGrade)