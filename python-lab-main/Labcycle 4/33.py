
class Bank:
    def __init__(self, account_number, name, account_type, balance):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit of {} successful".format(amount))
        print("Current balance is {}".format(self.balance))
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal of {} successful".format(amount))
            print("Current balance is {}".format(self.balance))

num=int(input("Enter account number: "))
name=input("Enter name: ")
acctype=input("Enter account type: ")
bal=int(input("Enter balance: "))
bnk=Bank(num,name,acctype,bal)
print("Account number: ",bnk.account_number)
print("Name: ",bnk.name)
print("Account type: ",bnk.account_type)
print("Balance: ",bnk.balance)
bnk.withdraw(int(input("Enter amount to withdraw: ")))
bnk.deposit(int(input("Enter amount to deposit: ")))
