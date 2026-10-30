balance = 10000

def check_balance():
    print("Your account balance is:", balance)


def deposit():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Money deposited successfully.")
        print("Available balance:", balance)
    else:
        print("Please enter a valid amount.")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Please enter a valid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance = balance - amount
        print("Please collect your cash.")
        print("Remaining balance:", balance)


def show_menu():
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice. Please try again.")
