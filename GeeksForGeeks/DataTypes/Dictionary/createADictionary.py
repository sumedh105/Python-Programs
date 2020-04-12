# Creating an empty dictionary
Dict = {}
print(Dict)

# Creating a dictionary with integer keys
DictOne = {1:"Sumedh", 2:"W.", 3:"Jambekar"}
print(DictOne)

# Creating a dictionary with string keys
DictTwo = {"Name":"Sumedh W. Jambekar", "DateOfBirth":"16-03-1987", "Country":"India"}
print(DictTwo)

# Creating a dictionary with mixed keys
DictThree = {"Name":"Sumedh W. Jambekar", 1:1987}
print(DictThree)

# Creating a dictionary with dict method
DictFour = dict({1:"Geeks", 2:"For", 3:"Geeks"})
print(DictFour)

# Creating a dictionary with dict method
DictFive = dict([(1, "Geeks"), (2, "For Geeks")])
print(DictFive)

# Creating a nested dictionary
DictSix = {"Website":"GeeksForGeeks", "Student":{"Name":"Sumedh W. Jambekar", "DoB":"16-03-1987", "Country":"India"}}
print(DictSix)
