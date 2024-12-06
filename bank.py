balance = 1000.00  # Starting balance
transactions = []  # List to store transaction history

def check_balance():
    print(f"\nYour current balance is: £{balance:.2f}")
    transactions.append("Checked balance.")

def deposit_money():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited £{amount:.2f}. New balance is £{balance:.2f}.")
            transactions.append(f"Deposited £{amount:.2f}.")
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def withdraw_money():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds!")
        elif amount > 0:
            balance -= amount
            print(f"Withdrew £{amount:.2f}. New balance is £{balance:.2f}.")
            transactions.append(f"Withdrew £{amount:.2f}.")
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_transactions():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for i, transaction in enumerate(transactions, 1):
            print(f"{i}. {transaction}")

def main():
    while True:
        print("\n--- Welcome to the BANK ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            print("Goodbye! Thanks for using the BANK.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

