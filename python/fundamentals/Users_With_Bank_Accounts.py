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

# Ben = BankAccount("Ben", "Checking", 500, .05)
# John = BankAccount("John", "Savings", 5000, .15)

# Ben.yield_interest()
# Ben.display_account_info()
# Ben.deposit(500).deposit(100).deposit(200).withdraw(50).yield_interest().display_account_info()
# John.deposit(1000).deposit(500).withdraw(50).withdraw(5).withdraw(25).withdraw(10).yield_interest().display_account_info()

# class User:		# declare a class and give it name User
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# guido = User()
# monty = User()

# print(guido.name)	# output: Michael
# print(monty.name)	# output: Michael

# guido.name = "Guido"
# monty.name = "Monty"

# print(guido.name)
# print(monty.name)

# class User:
#     def __init__(self, username, email_address):# now our method has 2 parameters!
#         self.name = username			# and we use the values passed in to set the name attribute
#         self.email = email_address		# and the email attribute
#         self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(name = name, account_type = "Checking",balance = 100, int_rate = .05)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)	# the specific user's account increases by the amount of the value received
    def make_withdrawl(self, amount):	# takes an argument that is the amount of the deposit
        self.account.withdraw(amount)	# the specific user's account increases by the amount of the value received
    def display_user_balance(self):
        print(self.account.balance)
    # def transfer_money(self,other_user,amount):           Can you use a method within a method within a class?
    #     self.make_withdrawl(self,amount)
    #     other_user.make_deposit(other_user,amount)
    #     print(self, self.display_user_balance())
    #     print(other_user, other_user.display_user_balance())

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
# guido.transfer_money(monty,50)


guido.display_user_balance()

