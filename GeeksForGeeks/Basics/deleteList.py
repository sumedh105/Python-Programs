# Create a new list
myList = []

# Add items to the list
myList.append("Sumedh W. Jambekar")
myList.append("16/03/1987")
myList.append("Gulbarga")
myList.append("Karnataka")
myList.append("India")

# Print a list before deletion
print(myList)

# Delete an element from a list
del myList[4]

# Print the list contents after deletion
print(myList)

# Print the list contents one by one
for index in range(4):
    print(myList[index])


