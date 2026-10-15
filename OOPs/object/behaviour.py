class InsufficientBalanceError(Exception):
    def __init__(self, message="Insufficient balance."):
        self.message = message
        super().__init__(self.message)
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):#instance method
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amt):#instance method
        #custom exception showing insufficient balance
        try:
            if amt > self.balance:
                raise InsufficientBalanceError()
        except InsufficientBalanceError as e:
            print(e)
        if 0 < amt <= self.balance:
            self.balance -= amt
            print(f"Withdrew {amt}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):#instance method
        return self.balance

    def __str__(self):#instance method
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

a1 = Account("2513152", "Rachit", 100000)
print(a1)
a1.deposit(5000)
print(a1)
a1.withdraw(10290)
print(a1)

