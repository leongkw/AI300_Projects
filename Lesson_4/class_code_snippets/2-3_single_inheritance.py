class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")


class SavingsAccount(BankAccount):  # inherits from BankAccount
    def __init__(self, account_holder_name, account_number, balance, interest_rate):
        # Call the superclass's initializer
        super().__init__(account_holder_name, account_number, balance)
        # Add additional instance attribute
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate


# Main program that uses inherited functionality

darren_account = SavingsAccount('Darren', 123456789, 1000, 0.01)
darren_account.deposit(5000)
print(darren_account.check_balance())       # 6000

print(darren_account.calculate_interest())  # 60.0, which is 1% of 6000
darren_account.withdraw(3000) 
print(darren_account.check_balance())       # 3000
