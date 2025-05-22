#Q5. Accept a number from the user and check whether it is prime or not.
# Expected Input: Enter a number : 11
# Expected Output : 11 is a prime number.

def checkPrime(n):
    count = 0
    for i in range(1,n):
        if n  % i == 0:
            count +=1
    if count < 2:
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")


def main():
    print("Enter a number : ",end="")
    num = int(input())
    checkPrime(num)

if __name__ == "__main__":
    main()