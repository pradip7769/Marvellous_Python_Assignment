# Q4. Accept a list of numbers and use reduce() (from functiools) to find the product of all numbers.
# Expected Input: Enter list : 2,3,4
# Expected Output: Product : 24

from functools import reduce

even = lambda a,b : a * b

def main():
    print("Enter the size of list : ")
    size = int(input())
    print("Enter list : ")
    Data = []
    for i in range(size):
        Data.append(int(input()))

    ret = reduce(even,Data)
    print("Product: ", ret)

if __name__ == "__main__":
    main()