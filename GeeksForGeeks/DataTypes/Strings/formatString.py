stringOne = "Hello Sumedh W. Jambekar"
print(stringOne)

# Default order
stringOne = "Hello {} {}. {}".format("Sumedh", "W", "Jambekar")
print(stringOne) 

# Positional formatting
stringOne = "Hello {1} {0}. {2}".format("W", "Sumedh", "Jambekar")
print(stringOne)

# Keyword formatting
stringOne = "Hello {0}, {middleName}, {lastName}".format("Sumedh", middleName = "W.", lastName = "Jambekar")
print(stringOne)
