#1. Create a list of items in your room you can potentially pack.
bedroom = ["Hat", "Shoes", "Sunscreen", "Socks"]
#2. Create an empty list to represent your travel bag 
travelBag = []
#3. Repeatedly prompt the user for the index of an item to put in their travel bag by removing it from the the list of items in your room to your travel bag list.
print("PACK YOUR BAGS")
print("Enter the index of an item you'd like to move from your room to your bag.")
print("Type '100' when you are done packing.\n")
print("Your Bedroom:")
print(bedroom)
item = int(input("Item Index: "))
while item != 100:
    travelBag.append(bedroom[item])
    bedroom.remove(bedroom[item])
    print("\nYour Bedroom:")
    print(bedroom)
    print("\nYour Travel Bag:")
    print(travelBag)
    item = int(input("Item Index: "))
#5. Print the contents of your luggage for the trip, as well as the number of items you decided to bring
print("\nYour finished luggage: ")
for item in travelBag:
    print(item)