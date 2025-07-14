student = {}

studentName = input("enter your student name: ")
student["name"] = studentName


studentAge = input("enter your student name: ")
student["age"] = studentAge


studentgrade = input("enter your student grade: ")
student["grade"] = studentgrade

habbies = []
hobby = input("enter your student habbies; type 'done' when finished: ").lower()
habbies.append(hobby)

while hobby != "done":
    hobby = input("enter your student habbies; type 'done' when finished: ").lower()
    hobby.append(hobby)
    
    student["habbies"] = habbies
    
    print(student)