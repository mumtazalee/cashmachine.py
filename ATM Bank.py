# ATM BANKING 
# If account no is "12345678","23456789", "34567890", "45678901", "56789012"
users = {
    "12345678": {"pin": "5678", "balance": 1000.0},
    "23456789": {"pin": "1234", "balance": 1500.0},
    "34567890": {"pin": "0000", "balance": 500.0},
    "45678901": {"pin": "1122", "balance": 800.0},
    "56789012": {"pin": "2233", "balance": 600.0}
    }

# Authenticate user by checking account number and PIN
def authenticate():
    print("Welcome to Your BANK!")
    account = input("Enter your Bank Account No: ")
    if account in users:
        pin = input("Enter your PIN: ")
        if users[account]["pin"] == pin:
            print(f"Login successful! Welcome to your Bank Account No: {account}.")
            return account
        else:
            print("Invalid PIN! Please try again.")
    else:
        print("Invalid Bank Account No! Please try again.")
    return None

# Show the users current balance
def check_balance(account):
        print(f"Your current balance is: £{users[account]['balance']:.2f}")

# Deposit money into the ussers account
def deposit(account):
    try:
        amount = float(input("Enter the ammount to deposit: "))
        if amount > 0:
            users[account]['balance'] += amount
            print(f"Deposited £{amount:.2f}. New balance: £{users[account]['balance']:.2f}")
        else:
            print("Deposit amount must be positive!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Withdraw money from the users account
def withdraw(account):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > users[account]['balance']:
            print("Insufficient funds in your Account!")
        elif amount > 0:
            users[account]['balance'] -= amount
            print(f"Withdraw £{amount:.2f}. New balance: £{users[account]['balance']:.2f}")
        else:
            print("Withdraw mount must be positive!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def atm_menu():
    account = authenticate()
    if not account:
        return

    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            check_balance(account)
        elif choice == '2':
            deposit(account)
        elif choice == '3':
            withdraw(account)
        elif choice == '4':
            print(f"Goodbye from your Bank, Account No: {account}! See you next time.")
            break
        else:
            print("Invalid option. Please try again.")

# Main Program
while True:
    atm_menu()
    exit_prompt = input("Do you want to exit the BANK? (yes/no): ").lower()
    if exit_prompt == "yes":
     print("Thank you for using your Bank. Goodbye!")
     break
