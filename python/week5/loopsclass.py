class GeniusList:
    
    
    
# step 1: crete a of every genius at your table
geniuses = [ "marshawn", "max", "avery", "semaj", "kauri", "devon"]

# step 2: loop through that list and print everyone's name to terminal
# what type of loop are we using here?
for genius in geniuses:
    print(genius)
    
# step 3: prompt the user to print the list again
answer = input("do you want me to print the list again? (Y/N): ")
while answer == "y":
    for genius in geniuses:
        print(genius)
    answer = input("do you want me to print the list again? (Y/N): ")
