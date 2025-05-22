
#Q1. Arithmetic Operations on Two Numbers
#   Write a program to accept two integers from the user and display their:
#   Sum, Difference, Product, Division
#Expected Input : Enter First number : 10  & Enter second number 2
#Expected Output : Sum : 12, Difference : 8, Product : 20, Division : 5.0

Sum = lambda value1,value2 : value1 + value2
Difference = lambda value1,value2 : value1 - value2
Product = lambda value1,value2 : value1 * value2
Division = lambda value1,value2 : value1 / value2

# def Sum(value1,value2):
#     return value1 + value2

# def Difference(value1,value2):
#     return value1 - value2

# def Product(value1,value2):
#     return value1 * value2

# def Division(value1,value2):
#     return value1 / value2

def main():
    print("Enter the firs number : ", end="")
    no1 = int(input())
    print("Enter the second number : ", end="")
    no2 = int(input())

    sum = Sum(no1,no2)
    diff = Difference(no1,no2)
    mul = Product(no1,no2)
    div = Division(no1,no2)

    print("Sum : ", sum)
    print("Difference : ", diff)
    print("Product : ", mul)
    print("Division : ", div)
    

if __name__ == "__main__":
    main()