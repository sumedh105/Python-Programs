import array

# Create an array
arr = array.array('i', [1, 2, 3, 4, 5, 6, 7])
# Printing an array
for index in range(len(arr)):
    print(arr[index])

print()

# Popping an element from an array
arr.pop(3)
# Printing an array
for index in range(len(arr)):
    print(arr[index])

print()

# Reversing an array
arr.reverse()
# Printing an array
for index in range(len(arr)):
    print(arr[index])

