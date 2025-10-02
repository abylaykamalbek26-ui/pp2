class Account:
    def __init__(self,balance,owner):
        self.balance = balance
        self.owner = owner
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"amount:{amount} . New balance{self.balance} ")
        else:  
            print("Amount of deposit must be positive")
    def withdraw(self,amount):
        if amount < self.balance and amount > 0:
            self.balance -= amount
            print(f"amount:{amount} . New balance{self.balance} ")
        else:
            print(f"Insufficient funds!Balance:{self.balance}")
    def __str__(self):
        return f"Account name:{self.owner}.Account balance:{self.balance}" 


acc = Account(1000,"Lebron")

acc.deposit(100)
acc.withdraw(200)
print(acc)