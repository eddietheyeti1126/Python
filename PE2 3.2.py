import doctest

class Bank_Account:
    """
    A simple bank account class with deposit, withdraw, and balance check functionality.

    >>> a = Bank_Account("Bob", 100)
    >>> type(a.account) == int
    True
    >>> a
    Bank_Account(name='Bob', Account Balance=100)
    >>> print(a)
    Account Name: Bob
    Account Balance: 100
    >>> a.deposit(150)
    150 deposited. New balance: 250
    >>> a.deposit(-30)
    Please deposit a positive number.
    >>> a.withdraw(200)
    200 withdrawn. New balance: 50
    >>> a.withdraw(70)
    Insufficient funds.
    >>> a.withdraw(-90)
    Please withdraw an amount greater than zero.
    >>> a.check_balance()
    Balance: 50
    """

    def __init__(self, Bob, starting_amount):
        self.Bob = Bob
        self.account = int(starting_amount)  # Ensure account balance is an integer

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
        if amount <= 0:
            print("Please withdraw an amount greater than zero.")
        elif amount > self.account:
            print("Insufficient funds.")
        else:
            self.account -= amount
            print(f"{amount} withdrawn. New balance: {self.account}")

    def check_balance(self):
        print(f"Balance: {self.account}")

if __name__ == "__main__":
    doctest.testmod(verbose=True)
