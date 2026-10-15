#bank class;employeee;customer;account -- aggregation and composition
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []  # Aggregation:bank has multiple account

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts

    def __str__(self):
        return f"Bank Name: {self.name}, Total Accounts: {len(self.accounts)}"
class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}"
class Customer:
    def __init__(self,customer_id,name):
        self.customer_id = customer_id
        self.name = name
        def __str__(self):
            return f"Customer ID: {self.customer_id}, Name: {self.name}"
class Account:
     def __init__(self,account_number,account_holder,balance=0):
         self.account_number = account_number
         self.account_holder = account_holder
         self.balance = balance

     def __str__(self):
         return f"Account Number: {self.account_number}, Holder: {self.account_holder}, Balance: {self.balance}"

#example usage
bank = Bank("MyBank")   
employee1 = Employee("E001", "DEEPAK")
customer1 = Customer("C001", "Rachit")
account1 = Account("2513152", "Rachit", 100000)
bank.add_account(account1)

employee2=Employee("2001","PRASHANT")
customer2=Customer("C002","RAHUL")
account2=Account("2513153","RAHUL",50000)
bank.add_account(account2)

print(bank.get_accounts())