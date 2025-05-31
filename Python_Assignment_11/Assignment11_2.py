#Q2 Factorisl Using Recursion Write a recursive function to calculate factorial of a number.
# factorial(5) --> 120

Fact = 1

def fact(n):
    global Fact
    if (n >= 1):
        fact(n - 1)
        Fact = Fact * n
    return Fact
       
def main():
   print("Enter the n number : ")
   no = int(input())
   Factorial = fact(no)
   print("Factorial is : ", Factorial)

if __name__ == "__main__":
    main()