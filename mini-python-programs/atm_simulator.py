tpin = "7777"
balance = 0

def welcome():
    print("Welcome to ATM")

def authenticate_pin():
    for attempt in range(3):
        pin = input("Enter your PIN: ")
        if pin == tpin:
            return True
        else:
            print("Incorrect PIN")
    print("Too many wrong attempts...")
    return False

def show_menu():
    print("\n----- ATM Menu -----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
    else:
        print("Invalid deposit amount.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
    else:
        print("Insufficient balance.")
    return balance

def check_balance(balance):
    print(f"Current balance: ${balance:.2f}")

def atm():
    global balance
    welcome()
    if not authenticate_pin():
        return
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            balance = deposit(balance)
        elif choice == "2":
            balance = withdraw(balance)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please try again.")

atm()