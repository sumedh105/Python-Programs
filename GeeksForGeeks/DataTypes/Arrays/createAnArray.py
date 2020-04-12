import array

# Creating an array
arr = array.array('i', [1, 2, 3, 4, 5])
# Print an array
for index in range(len(arr)):
    print(arr[index])

print()

# Append an integer to an array using append() function
arr.append(6)
# Print an array
for index in range(len(arr)):
    print(arr[index])

print()

# Insert an element at a specific position in an array using insert() function
arr.insert(4, 9)
# Print an array
for index in range(len(arr)):
    print(arr[index])
