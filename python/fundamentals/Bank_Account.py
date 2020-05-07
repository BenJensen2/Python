class BankAccount:
    def __init__(self, name, account_type, balance, int_rate): # don't forget to add some default values for these parameters!
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.int_rate = int_rate
        # your code here! (remember, this is where we specify the attributes for our class)
        # # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
        # your code here
    def withdraw(self, amount):
        self.balance -= amount
        return self
        # your code here
    def display_account_info(self):
        print(self.name)
        print(self.account_type)
        print(self.balance)
        print(self.int_rate)
        return self
        # your code here
    def yield_interest(self):
        self.balance = self.balance * self.int_rate + self.balance
        return self
        # your code here

Ben = BankAccount("Ben", "Checking", 500, .05)
John = BankAccount("John", "Savings", 5000, .15)

# Ben.yield_interest()
# Ben.display_account_info()
Ben.deposit(500).deposit(100).deposit(200).withdraw(50).yield_interest().display_account_info()
John.deposit(1000).deposit(500).withdraw(50).withdraw(5).withdraw(25).withdraw(10).yield_interest().display_account_info()