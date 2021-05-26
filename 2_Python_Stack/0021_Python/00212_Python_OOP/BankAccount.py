"""
Create a BankAccount class with the attributes interest rate and balance
Add a deposit method to the BankAccount class
Add a withdraw method to the BankAccount class
Add a display_account_info method to the BankAccount class
Add a yield_interest method to the BankAccount class
Create 2 accounts
To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)
"""
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
            print ("Insufficient funds. Charing $5 overdraft fee")
            self.balance -= 5
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

firstAccount = BankAccount(0.015, 5000)
secondAccount = BankAccount(0.010, 4500)

firstAccount.deposit(100).deposit(200).deposit(300).withdraw(150).yield_interest().display_account_info()
print("******************************")
secondAccount.deposit(500).deposit(1000).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()
"""solutions
You have deposited 100 dollars
You have deposited 200 dollars
You have deposited 300 dollars
Withdrawing 150 dollars
You have earned 81.75 dollars in interest
The account balance is 5531.75 dollars.
******************************
You have deposited 500 dollars
You have deposited 1000 dollars
Withdrawing 100 dollars
Withdrawing 200 dollars
Withdrawing 300 dollars
Withdrawing 400 dollars
You have earned 50.0 dollars in interest
The account balance is 5050.0 dollars.
"""