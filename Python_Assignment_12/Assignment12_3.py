# Q3 Write a program which contains one class named as arith1metic. 
# arith1metic class contains three instance variable as Value1, value2. 
# Inside init method initialise all instance variables to 0. 
# There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division(). 
# Accept method will accept value of Value1, Value2 from user. 
# Addition() method will perform addition of Value1, Value2 and return result.
# Subtraction() method will perform Subtraction of Value1, Value2 and return result.
# Multiplication() method will perform Multiplication of Value1, Value2 and return result.
# Division() method will perform Division of Value1, Value2 and return result.
# After designing the above class call all instance methos by creating multiple objects. 

class arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        print("Enter the First Value : ", end="")
        self.Value1 = int(input())
        print("Enter the second value : ",end="")
        self.Value2 = int(input())
    
    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2


def Display(add,sub,mul,div):
    print("Addition is : ", add)
    print("Subtraction is : ", sub)
    print("Multiplication is : ", mul)
    print("Division is : ", div)

def main():

    arith1 = arithmetic()

    arith1.Accept()
    add = arith1.Addition()
    sub = arith1.Subtraction()
    mul = arith1.Multiplication()
    div = arith1.Division()

    Display(add,sub,mul,div)

    arith2 = arithmetic()

    arith2.Accept()
    add = arith2.Addition()
    sub = arith2.Subtraction()
    mul = arith2.Multiplication()
    div = arith2.Division()

    Display(add,sub,mul,div)

if __name__ == "__main__":
    main()

        