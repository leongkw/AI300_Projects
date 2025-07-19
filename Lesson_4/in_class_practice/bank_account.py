class BankAccount:
    bank_details = {'name' : 'Bank of Dog'}

    def __init__(self, account_holder_name: str, account_number: int, balance: float):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def welcome(self):
        print('Welcome {}!'.format(self.account_holder_name))

    def get_balance(self):
        return round(self.balance, 2)
    
    def deposit_funds(self, amount: float):
        self.balance += amount

    # In-Class Practice 1.11.1: Add an instance method
    def withdraw_funds(self, amount: float):
        if amount > self.balance:
            print('Insufficient Funds')
        else:
            self.balance -= amount

# Instantiate bank account of dog
dog = BankAccount('Dog', 123, 55.6)

# Print welcome message of dog
dog.welcome()

# Print bank account balance of dog
print(dog.get_balance())

# Add 100 dollars into bank account of dog
dog.deposit_funds(100)
print(dog.get_balance())

# Withdrawing 200 and 100 dollars from bank account of dog
dog.withdraw_funds(200)
print(dog.get_balance())

dog.withdraw_funds(100)
print(dog.get_balance())
