class BankAccount:
    def __init__(self):
        self.owner = None
        self.balance = 0
    def deposit(self, owner, initial_deposit):
        if self.owner is not None:
            print("Account already exists.")
            return
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
        self.owner = owner
        self.balance = initial_deposit
        print(f"Account created for {owner} with initial deposit of ${initial_deposit}.")
    def withdraw(self, amount):
        if self.owner is None:
            print("No account exists. Please create an account first.")
            return
        if amount < 0:
            print("Withdrawal amount cannot be negative.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance: ${self.balance}.")
    def display_balance(self):
        if self.owner is None:
            print("No account exists. Please create an account first.")
            return
        print(f"Account owner: {self.owner}, Balance: ${self.balance}.")    

account1=BankAccount()
account1.deposit("Alice", 1000)
account1.display_balance()
account1.withdraw(200)
account1.display_balance()
account1.withdraw(900)
account1.display_balance()        