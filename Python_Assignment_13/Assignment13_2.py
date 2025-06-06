
# Q2 Write a program which contains one class named as BankAccount. 
# BankAccount class contains two instance Variables as Name and Amount. 
# That class contains one class variable as ROI which is initialise to 10.5 
# Inside init mehtod initialise all name and amount variables by acvepting the values from user. 
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest(). 
# Deposit() method will accept the amount from user and add that value in class instance variable Amount. 
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount. 
# CaluclateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI. 
# And Display() method will display value of all the instance variables as name and Amount. 
# After designing the above calss call all instance methods by creating multiple objects. 


class BankAccount:
    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("BAC Name : ", self.Name)
        print("Amount : ", self.Amount)

    def Deposit(self):
        print("Enter the Deposit Amount : ",end="")
        D_Amount = int(input())
        self.Amount += D_Amount

    def Withdraw(self):
        print("Enter the Withdraw Amount : ",end="")
        W_Amount = int(input())
        self.Amount -= W_Amount
        print(W_Amount,"Withdrawn. New Balance is : ", self.Amount)

    def CalculateIntrest(self):
        interest = (self.Amount * BankAccount.ROI) / 100 
        print(f"Interest on ₹{self.Amount} at ROI {BankAccount.ROI}% = ₹{interest:.2f}")



def main():

    acc1 = BankAccount("Pradip", 1000)
    acc1.Deposit()
    acc1.Display()
    acc1.Withdraw()
    acc1.CalculateIntrest()
    acc1.Display()

    print("-" * 30)

    acc2 = BankAccount("PR",2000)
    acc2.Deposit()
    acc2.Display()
    acc2.Withdraw()
    acc2.CalculateIntrest()
    acc2.Display()

    print("-" * 30)


if __name__ == "__main__":
    main()
    
        

