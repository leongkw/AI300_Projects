class CreditCard:
    def __init__(self, cc_number, credit_limit):
        self.account_number = cc_number
        self.credit_limit = credit_limit
        self.balance = 0

    def get_balance(self):
        return self.balance

    def get_credit_limit(self):
        return self.credit_limit

    
    def set_credit_limit(self, new_credit_limit):
        if new_credit_limit < 0 or new_credit_limit > 100_000:
            print("Credit limit cannot be negative or more than $100,000.")
        else:
            self.credit_limit = new_credit_limit

    def make_purchase(self, amount):
        available_credit = self.credit_limit - self.balance
        if amount < 0 or amount > available_credit:
            print("Purchase amount must not be negative or exceed available credit.")
        else:
            self.balance += amount
    
    def make_payment(self, amount):
        if amount < 0:
            print("Payment amount cannot be negative.")
        else:
            self.balance = max(self.balance - amount, 0)