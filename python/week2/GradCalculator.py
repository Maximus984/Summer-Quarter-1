numberGrade = int(input("enter a number grade from 0 to 100: "))
lettergrade = ""

if (numberGrade >= 90):
    lettergrade = "A"
elif (80 <= numberGrade < 89):
    lettergrade = "B"
elif (70 <= numberGrade < 79):
    lettergrade = "C"
elif (60 <= numberGrade < 69):
    lettergrade = "D"
elif (numberGrade < 60):
    lettergrade = "F"
print("you got a "+ lettergrade)
    

