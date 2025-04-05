class Bank_Account:
    def __init__(self, name, starting_amount):
        self.name = name
        self.account = starting_amount

    def __repr__(self):
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})"

    def __str__(self):
        return f"Account Name: {self.name}\nAccount Balance: {self.account}"

    def deposit(self, amount):
        if amount > 0:
            self.account += amount
            print(f"{amount} deposited. New balance: {self.account}")
        else:
            print("Please deposit a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if self.account - amount >= 0:
                self.account -= amount
                print(f"{amount} withdrawn. New balance: {round(self.account, 2)}")
            else:
                print("Insufficient funds.")
        else:
            print("Please withdraw an amount greater than zero.")

    def check_balance(self):
        print(f"Balance: {self.account}")


class SavingsAccount(Bank_Account):
    def __init__(self, name, balance, interest_rate=1.0):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def __repr__(self):
        return f"SavingsAccount(account_holder='{self.name}', balance={int(self.account)}, interest_rate={self.interest_rate}%)"

    def __str__(self):
        return f"Savings Account - {self.name}: Balance = ${self.account:.2f}, Interest Rate = {self.interest_rate}%"

    def apply_interest(self):
        interest = self.account * (self.interest_rate / 100)
        self.account += interest
        return round(self.account, 2)


class CheckingAccount(Bank_Account):
    def __init__(self, name, balance, overdraft_limit=100.0):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def __repr__(self):
        return f"CheckingAccount(account_holder='{self.name}', balance={int(self.account)}, overdraft_limit={self.overdraft_limit})"

    def __str__(self):
        return f"Checking Account - {self.name}: Balance = ${self.account:.2f}, Overdraft Limit = ${self.overdraft_limit:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.account + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.account -= amount
            if self.account % 1 == 0:
                print(int(self.account))
            else:
                print(round(self.account, 2))


# Show output like the instructions
if __name__ == "__main__":
    print(">>> a = SavingsAccount('bob', 100)")
    a = SavingsAccount("bob", 100)
    print(">>> print(a)")
    print(a)
    print(">>> a")
    print(repr(a))
    print(">>> a.apply_interest()")
    print(a.apply_interest())

    print(">>> a = SavingsAccount('bob', 12345)")
    a = SavingsAccount("bob", 12345)
    print(">>> a.apply_interest()")
    print(a.apply_interest())

    print(">>> a = CheckingAccount('bob', 100)")
    a = CheckingAccount("bob", 100)
    print(">>> print(a)")
    print(a)
    print(">>> a")
    print(repr(a))
    print(">>> a.withdraw(-20)")
    a.withdraw(-20)
    print(">>> a.withdraw(230.0)")
    a.withdraw(230.0)
    print(">>> a.withdraw(30)")
    a.withdraw(30)

    print(">>> a = SavingsAccount('bob', 12345)")
    a = SavingsAccount("bob", 12345)
    print(">>> a.withdraw(130)")
    a.withdraw(130)
    print(">>> a.withdraw(854.34)")
    a.withdraw(854.34)
