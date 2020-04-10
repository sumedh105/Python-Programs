def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    return (a / b)

def MAIN():
    print("Enter two numbers: ")

    a = int(input("Enter the first number: "))
    print("The first number entered is: ", a)

    b = int(input("Enter the second number: "))
    print("The second number entered is: ", b)

    print("Enter 1 for addition: ")
    print("Enter 2 for subtraction: ")
    print("Enter 3 for multiplication: ")
    print("Enter 4 for division: ")

    choice = int(input("Enter your choice: "))
    print("The choice entered is: ", choice)

    if (choice == 1):
        result = add(a, b)
    elif (choice == 2):
        result = subtract(a, b)
    elif (choice == 3):
        result = multiply(a, b)
    elif (choice == 4):
        result = divide(a, b);

    print("The result is: ", result)

if __name__ == "__main__":
    MAIN()
