import keyword

keys = ["Sumedh", "for", "while", "in", "is", "Jambekar"]

for index in range(len(keys)):
    if (keyword.iskeyword(keys[index])):
        print("The key is a keyword")
    else:
        print("The key is not a keyword")
