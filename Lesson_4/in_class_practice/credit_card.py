# In-Class Practice 1.11.2: Write your own class from scratch
class CreditCard:
    bank_details = {'name' : 'Bank of Dog'}

    def __init__(self, cc_number: int, credit_limit: float, balance: float = 0):
        self.cc_number = cc_number
        self.__balance = balance
        if 0 <= credit_limit <= 100000:
            self.__credit_limit = credit_limit
        else:
            print('Error. Credit limit must be greater than $0 and less than $100,000.')

    def check_balance(self):
        return self.__balance
    
    def check_credit_limit(self):
        return self.__credit_limit
    
    def set_new_credit_limit(self, credit_limit: float):
        if credit_limit < 0 or credit_limit > 100000:
            print('Error. New credit limit must be greater than $0 and less than $100,000.')
        else:
            self.__credit_limit = credit_limit
    
    def make_purchase(self, amount: float):
        if amount < 0 or amount > (self.__credit_limit - self.__balance):
            print('Error. Unable to make purchase of ${}'.format(amount))
        else:
            self.__balance += amount
    
    def make_payment(self, amount):
        if amount < 0:
            print('Error. Unable to make a negative payment.')
        elif amount > self.__balance:
            self.__balance = 0
        else:
            self.__balance -= amount
            print('Payment of ${} made. New balance of ${}.'.format(amount, self.__balance))   

# Instantiate credit card for dog
dogcard = CreditCard(1234, 100000)

# Check balance for dog's credit card
print(dogcard.check_balance())

# Check credit limit for dog's credit card
print(dogcard.check_credit_limit())

# Set new credit limit for dog's credit card
# Set 200,000 and 50,000
dogcard.set_new_credit_limit(200000)
print(dogcard.check_credit_limit())

dogcard.set_new_credit_limit(50000)
print(dogcard.check_credit_limit())

# Make purchase with dog's credit card
# Make purchase of -$5, $200,000 and $100
dogcard.make_purchase(-5)
print(dogcard.check_balance())

dogcard.make_purchase(200000)
print(dogcard.check_balance())

dogcard.make_purchase(100)
print(dogcard.check_balance())

# Make payment to dog's credit card
# Make payment of -5, 50, 100
dogcard.make_payment(-5)
print(dogcard.check_balance())

dogcard.make_payment(50)
print(dogcard.check_balance())

dogcard.make_payment(100)
print(dogcard.check_balance())

# my_credit_card = CreditCard(123456789, 5000)
# assert my_credit_card.cc_number == 123456789
# assert my_credit_card.check_balance() == 0
# assert my_credit_card.check_credit_limit() == 5000

# my_credit_card.set_new_credit_limit(1000)
# my_credit_card.set_new_credit_limit(-1)       # print error
# my_credit_card.set_new_credit_limit(100001)   # print error
# assert my_credit_card.check_credit_limit() == 1000

# my_credit_card.make_purchase(900)
# my_credit_card.make_purchase(-1)          # print error
# my_credit_card.make_purchase(200)         # print error
# assert my_credit_card.check_balance() == 900

# my_credit_card.make_payment(500)
# assert my_credit_card.check_balance() == 400

# my_credit_card.make_payment(5000)
# assert my_credit_card.check_balance() == 0

# print("All tests passed!")