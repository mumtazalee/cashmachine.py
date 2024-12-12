# ATM BANKING 
# If account no is "12345678" or "23456789"
users = {
    "12345678": {"pin": "5678", "balance": 1000.0},
    "23456789": {"pin": "1234", "balance": 500.0}
    }

def authenticate():
    print("Welcome to your BANK!")
    user_id = input("Enter Account No: ")
    if user_id in users:
        pin = input("Enter PIN: ")
        if users[user_id]["pin"] == pin:
            print(f"Login successful! Welcome to your Account No: {user_id}.")
            return user_id
        else:
            print("Invalid PIN!")
    else:
        print("Invalid Bank Account No!")
    return None

def check_balance(user_id):
        print(f"Your balance is: £{users[user_id]['balance']:.2f}")

def deposit(user_id):
    try:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            users[user_id]['balance'] += amount
            print(f"Deposited £{amount:.2f}. New balance: £{users[user_id]['balance']:.2f}")
        else:
            print("Amount must be positive!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def withdraw(user_id):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount > users[user_id]['balance']:
            print("Insufficient funds!")
        elif amount > 0:
            users[user_id]['balance'] -= amount
            print(f"Withdrew £{amount:.2f}. New balance: £{users[user_id]['balance']:.2f}")
        else:
            print("Amount must be positive!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def atm_menu():
    user_id = authenticate()
    if not user_id:
        return

    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            check_balance(user_id)
        elif choice == '2':
            deposit(user_id)
        elif choice == '3':
            withdraw(user_id)
        elif choice == '4':
            print(f"Goodbye from you Bank, Account No: {user_id}!")
            break
        else:
            print("Invalid option. Try again.")

# Main Program
if __name__ == "__main__":
    while True:
        atm_menu()
        exit_prompt = input("Exit BANK? (yes/no): ").lower()
        if exit_prompt == "yes":
            print("Thank you for using your Bank. Goodbye!")
            break
