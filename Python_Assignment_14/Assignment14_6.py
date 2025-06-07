# Create a class calculator with methods for add, subtract, multiply, divide. 
# Ask user input for values and call methods accordingly. 

class Calculator:
    def __init__(self,value1,value2):
        self.v1 = value1
        self.v2 = value2
    
    def Add(self):
        sum = self.v1 + self.v2
        print("Addtion is : ", sum)
    
    def Sub(self):
        sub = self.v1 - self.v2
        print("Subtraction is : ", sub)
    
    def Mul(self):
        mul = self.v1 * self.v2
        print("multiplication is : ", mul)
    
    def Div(self):
        div = self.v1 / self.v2
        print(f"Division is : {div:.2f}")

    
def main():
    print("Enter the First value : ", end="")
    value1 = int(input())
    print("Enter the second value : ", end="")
    value2 = int(input())

    print("Choose the Operation : ")
    print("1. Addition \n2.Subtraction \n3. Multiplication \n4. Division")
    choice = input()

    calc = Calculator(value1,value2)

    if choice == "1":
        calc.Add()
    elif choice == "2":
        calc.Sub()
    elif choice == "3":
        calc.Mul()
    elif choice == "4":
        calc.Div()
    else:
        print("Choose the correct number ...")


if __name__ == "__main__":
    main()