class Account:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def __str__(self):
        return f"Account Number: {self.account_number}\nOwner: {self.owner}\nBalance: ${self.balance:.2f}"

class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0.0, interest_rate=0.01):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Interest of ${interest_amount:.2f} applied. New balance is ${self.balance:.2f}.")

class CheckingAccount(Account):
    def __init__(self, account_number, owner, balance=0.0, overdraft_limit=100.0):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                print(f"Withdrawal of ${amount} successful. New balance is ${self.balance}.")
            else:
                print("Withdrawal amount exceeds overdraft limit.")
        else:
            print("Withdrawal amount must be greater than zero.")

# Example usage of the banking application
if __name__ == "__main__":
    # Create a savings account
    savings = SavingsAccount("SAV-001", "Alice", 1000.0, 0.02)
    print(savings)
    savings.deposit(500.0)
    savings.apply_interest()
    savings.withdraw(200.0)

    print("\n")

    # Create a checking account
    checking = CheckingAccount("CHK-001", "Bob", 500.0, 200.0)
    print(checking)
    checking.deposit(300.0)
    checking.withdraw(700.0)
