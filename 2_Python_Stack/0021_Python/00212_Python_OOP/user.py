class User:
    """ A customer of The Uhuru Bank with a checking account. 
        has the following attributes:
        - firstName: A string representing the customer's first name
        - lastName: A string representing the customer's last name.
        - email: a string representing the customer's email address
        - balance: A float tracking the customer's account balance 
    """
    def __init__(self, first_name, last_name, email_address, account_balance = 0.0):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email_address
        self.balance = account_balance

    def make_deposit(self, amount):
        self.balance += amount
        return self.balance

    def make_withdrawal(self, amount):
        if amount > self.balance:
            print("Amount greater than available balance.")
            return 
        self.balance -= amount
        return self.balance

    def display_user_balance(self):
        return self.balance
    
    
    def transfer_money(self, amount, transfUser):
        if amount > self.balance:
            print("Impossible Endeavor.")
            return 
        self.balance -= amount
        transfUser.balance += amount



user1 = User("John", "Loft", "john@coding.com", 1000.0)
user2 = User("Kathy", "Fruit", "kathy@dojo.ru", 500.0)
user3 = User("Franck","April", "kathy@paris.fr", 700.0)

user1.make_deposit(200)
user1.make_deposit(150)
user1.make_deposit(100)
user1.make_withdrawal(300)
print(user1.display_user_balance())
#solution:1150.0

user2.make_withdrawal(50)
user2.make_withdrawal(150)
user2.make_deposit(200)
print(user2.display_user_balance())
#solution:500.

user3.make_deposit(250)
user3.make_withdrawal(50)
user3.make_withdrawal(150)
user3.make_withdrawal(200)
print(user3.display_user_balance())
#solution:550

user1.transfer_money(350, user2)
print(user1.display_user_balance())
#solution:800.0
print(user2.display_user_balance())
#solution:850.0
