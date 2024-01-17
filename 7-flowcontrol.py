
maths,physics, chemistry= input("Enter marks of maths, physics & chemistry:").split()
mathsInt = int(maths)
physicsInt = int(physics)
chemistryInt = int(chemistry)
Grade = 'F'

if (not(mathsInt <35 or physicsInt <35 or chemistryInt <35) ):
    totalMarks = mathsInt+physicsInt+chemistryInt
    averageMarks = totalMarks/3
    if(averageMarks <= 59):
        Grade = 'C'
    elif(averageMarks <= 69):
        Grade = 'B'
    else:
        Grade = 'A'
print("Grade "+ Grade)