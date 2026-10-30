# Simple Calculator

def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Addition:", a + b)


def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Subtraction:", a - b)


def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Multiplication:", a * b)


def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if b == 0:
        print("Cannot divide by zero.")
    else:
        print("Division:", a / b)


while True:

    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addition()

    elif choice == "2":
        subtraction()

    elif choice == "3":
        multiplication()

    elif choice == "4":
        division()

    elif choice == "5":
        print("Thank you for using Simple Calculator!")
        break

    else:
        print("Invalid option! Please try again.")
