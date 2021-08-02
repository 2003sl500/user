class User:
    # delaring a class attribute (bank_name)
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        # declaring instance attributes
        self.name = name
        self.email = email_address
        self.account_balance = 0

danielName = "Daniel Shoemaker"
adrianName = "Adrian Acosta"
keithName = "Keith Hastings"

daniel = User(danielName, "danielshoe@charter.net")
adrian = User(adrianName, "adrian@something.com")
keith = User(keithName, "keith@something.com")

def make_deposit(self, amount):
    self.account_balance += amount

def make_withdrawl(self, amount):
    self.account_balance -= amount

def transfer_money(from_user, to_user, amount):
    make_withdrawl(from_user, amount)
    make_deposit(to_user, amount)

def display_user_balance(self):
    print("User:", self.name, ", Balance: $" + str(self.account_balance))

make_deposit(daniel, 1000)
make_deposit(daniel, 250)
make_deposit(daniel, 500)
make_withdrawl(daniel, 150)
display_user_balance(daniel)

make_deposit(adrian, 1500)
make_deposit(adrian, 1000)
make_withdrawl(adrian, 300)
make_withdrawl(adrian, 125)
display_user_balance(adrian)

make_deposit(keith, 1500)
make_withdrawl(keith, 150)
make_withdrawl(keith, 100)
make_withdrawl(keith, 200)
display_user_balance(keith)

transfer_money(daniel, keith, 250)
display_user_balance(daniel)
display_user_balance(keith)