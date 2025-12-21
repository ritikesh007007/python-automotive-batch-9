class BankAccount:
    def _init_(self,account_number,custmoer_name,initial_balance=0.0):
        self.account_number=account_number
        self.customer_name=custmoer_name
        self.balance=initial_balance
       
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        self.balance-=amount
        
account=BankAccount("101","Ritikesh kumar",1000.0)

account.deposit(500.0)