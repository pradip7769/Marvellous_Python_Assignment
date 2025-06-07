# Create a class BankAccount with account_number, name, and balance. 
# Use __init__ and create a methods for deposit, withdraw, and displaying balance. 

class BankAccount:
    def __init__(self,account_number,name,balance):
        self.ac_no = account_number
        self.name = name 
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(amount,"deposited successfully...")
    
    def withdraw(self,amount):
        self.balance -= amount
        print(amount,"Withdraw successfully")
    
    def display(self):
        print("Available balance is : ", self.balance)
    

def main():
    customer = BankAccount("SB23423","PR",10000)
    customer.deposit(5000)
    customer.display()
    customer.withdraw(7000)
    customer.display()

if __name__ == "__main__":
    main()
