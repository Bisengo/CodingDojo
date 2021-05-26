class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)    # added this line

    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
        #print(self.account.balance)     # or access its attributes



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
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print ("Amount greater than available balance.")
            return
        else:
            print (f"Withdrawing {amount} dollars")
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"The account balance is {self.balance} dollars.")
        return self

    def yield_interest(self):
        if self.balance <= 0:
            print("No Interest Earned.")
            return
        else:
            interest = self.balance * self.interest
            print (f"You have earned {interest} dollars in interest")
            self.balance += interest
        return self

