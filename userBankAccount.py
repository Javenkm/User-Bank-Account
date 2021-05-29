class BankAccount:
    def __init__(self, int_rate, balance): # don't forget to add some default values for these parameters!
        # your code here! (remeber, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount): # increases the account balance by the given amount
        self.balance += amount
        return self
    
    def withdraw(self, amount): # decreases the account balance by the givena amount if there are sufficient funds; if there is not 
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insuffucient funds: Charging a $2.50 fee")
            self.balance -= 2.50
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
    
    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate = 0.011, balance = 0)
        # self.account2 = BankAccount ("savings", int_rate = 0.02, balance = 0) would use this to add separate account
    
    def transfer_money(self, amount, other_user):
        self.account.balance = self.account.balance - amount
        other_user.account.balance = other_user.account.balance + amount
        print(f"Name: {self.name} transferred {amount} dollars to {other_user.name}")
        return self

    def display_account_info(self):
        print(f"Name: {self.name}, {self.account.display_account_info()}")
        return self

Javen = User("Javen", "javenkm@gmail.com")
Israel = User("Israel", "Broheim@codingdojo.com")
Ella = User("Ella", "Ellaisawesome@codingdojo.com")

Javen.account.deposit(105000)
Javen.display_account_info()
Israel.account.deposit(5380)
Israel.display_account_info()
Ella.account.deposit(1300)
Ella.display_account_info()
Javen.transfer_money(1000, Israel)
Israel.display_account_info()