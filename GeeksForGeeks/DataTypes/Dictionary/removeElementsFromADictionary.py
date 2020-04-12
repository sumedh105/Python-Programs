# Create a dictionary
dictOne = {"Name":"Sumedh W. Jambekar", "DoB":"16-03-1987", "State":"Karnataka", "Place":"Kalaburagi", "Country":"India"}
print(dictOne)

# Removing from a dictionary using del keyword
del dictOne["Name"]
print(dictOne)

# Removing from a dictionary using pop() method
popElement = dictOne.pop("DoB")
print(dictOne)

# Removing from a dictionary using popitem() method
poppedEle = dictOne.popitem()
print(dictOne)

# Removing from a dictionary using clear() method. This method deletes an entire dictionary
dictOne.clear()
print(dictOne)
