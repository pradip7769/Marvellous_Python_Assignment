# Q2. Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum of all even numbers from 1 to 100
# Expected Output : Sum of even numbers between 1 to 100 is : 2550

from functools import reduce

def numlist():
    num = []
    for i in range(101):
        num.append(i)
    return num

def even(value):
    return value % 2 == 0

def REDUCE(value):
    sum = 0
    for i in value:
        sum += i
    return sum


def main():
   numbers =  numlist()
   FData = list(filter(even, numbers))
#    print(FData)
   RData = REDUCE(FData)
   print("Sum of even number is : ", RData)

if __name__ == "__main__":
    main()


