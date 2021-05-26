"""
Update the User class __init__ method
Update the User class make_deposit method
Update the User class make_withdrawal method
Update the User class display_user_balance method
SENSEI BONUS: Allow a user to have multiple accounts; update methods so 
the user has to specify which account they are withdrawing or depositing to
"""
class User:
    def __init__(self, first_name, last_name, email_address):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email_address
        self.checking_account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.checking_account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.checking_account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.checking_account.display_account_info()
        return self
    
    def transfer_money(self, amount, transfName):
        self.account.transfer_money(amount, transfName)
        print(self.account.balance)
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print ("You have no money")
            return
        else:
            print (f"You have deposited {amount} dollars")
            self.balance += amount
        #return self

    def withdraw(self, amount):
        if amount > self.balance:
            print ("Amount greater than available balance.")
            return
        else:
            print (f"Withdrawing {amount} dollars")
            self.balance -= amount
        #return self

    def display_account_info(self):
        print(f"The account balance is {self.balance} dollars.")
        #return self

    def yield_interest(self):
        if self.balance <= 0:
            print("No Interest Earned.")
            return
        else:
            interest = self.balance * self.interest
            print (f"You have earned {interest} dollars in interest")
            self.balance += interest
        #return self

    def transfer_money(self, amount, transfName):
        if amount > self.balance:
            print("Impossible Endeavor.")
            return 
        self.balance -= amount
        transfName.account.balance += amount
        #return self

Mutombo = User("Mutombo", "Dikembe", "mutombo@python.fr")
print(Mutombo.make_deposit(1000)) # using class User method
print("********************")
print(Mutombo.checking_account.deposit(1000)) # using class BankAccount method
print("********************")
print("********************")
print(Mutombo.make_withdrawal(250))
print("********************")
print(Mutombo.checking_account.withdraw(250))
print("********************")
print(Mutombo.checking_account.display_account_info())