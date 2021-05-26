class User:
    def __init__(self, first_name, last_name, email_address, account_balance = 0.0):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email_address
        self.balance = account_balance
    
John = User("John", "Loft", "john@coding.com", 1000.0)
Kathy = User("Kathy", "Fruit", "kathy@dojo.ru", 500.0)
Franck = User("Franck", "April", "kathy@paris.fr", 700.0)
print(John.balance)    