# Q4. Accept a number and print its factorial using a for loop.
# Expected Input: Enter a number : 5
# Expected Output : Factorial of 5 is : 120

def fact(n):
    Fact = 1
    for i in range(1,n+1):
        Fact = Fact * i

    print("Factorial of",n,"is : ",Fact)

def main():
    print("Enter a number : ",end="")
    num = int(input())
    fact(num)

if __name__ == "__main__":
    main()