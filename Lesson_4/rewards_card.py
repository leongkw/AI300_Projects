class CreditCard:
    bank_details = {'name' : 'Bank of Cat'}

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

class RewardsCard(CreditCard):
    def __init__(self, cc_number: int, credit_limit: float, rewards_rate: float, balance: float = 0):
        super().__init__(cc_number, credit_limit, balance) 
        self.rewards_rate = rewards_rate
        self.__reward_points = 0

    def make_purchase(self, amount: float):
        previous_balance = self.check_balance()
        super().make_purchase(amount)
        current_balance = self.check_balance()
        # If balance changed, means purchase successful
        if previous_balance != current_balance:
            earned_points = amount * self.rewards_rate
            self.__reward_points += earned_points

    def check_reward_points(self):
        return self.__reward_points
    
    def redeem_reward_points(self, points: float):
        if points < 0:
            print ('Error. Cannot redeem negative amount of points')
        elif points > self.__reward_points:
            print('Redeemed points exceeds rewards points balance.')
        else:
            self.__reward_points -= points
            print('Redeemed {} points. {} points remaining'.format(points, self.__reward_points))


# Instantiate rewards card for cat
cat_rewards_card = RewardsCard(1234, 100000, 0.1)

# Check credit limit for rewards card of cat
print(cat_rewards_card.check_credit_limit())

# Check balance for rewards card of cat
print(cat_rewards_card.check_balance())

# Make purchase of 100
# Check balance, then check reward points
cat_rewards_card.make_purchase(100)
print(cat_rewards_card.check_balance())
print(cat_rewards_card.check_reward_points())

# Make purchase of -5
# Check balance, then check reward points
mouse_rewards_card = RewardsCard(1234, 100000, 0.1)
mouse_rewards_card.make_purchase(-5)
print(mouse_rewards_card.check_balance())
print(mouse_rewards_card.check_reward_points())

# Redeem -5 points, then redeem 5 points
cat_rewards_card.redeem_reward_points(-5)
print(cat_rewards_card.check_reward_points())

cat_rewards_card.redeem_reward_points(5)
print(cat_rewards_card.check_reward_points())





