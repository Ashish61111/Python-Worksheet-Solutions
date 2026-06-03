class BankAccount:

    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("₹", amount, "deposited successfully.")
        print("Updated Balance: ₹", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully.")
            print("Remaining Balance: ₹", self.balance)

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

account_number = input("Enter Account Number: ")
account_holder_name = input("Enter Account Holder Name: ")
balance = float(input("Enter Initial Balance: "))
account = BankAccount(account_number, account_holder_name, balance)
while True:

    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        print("Thank you for using the Bank System.")
        break

    else:
        print("Invalid Choice! Please try again.")