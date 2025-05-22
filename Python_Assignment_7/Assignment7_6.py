# Q6. Write a function that accepts a list of integers and returns a list of prime numbers using filter(). 
# Expected Input: Enter list : 10 11 12 13 14 15 16 17
# Expected Output : [11,13,17]

def checkPrime(n):
    count = 0
    for i in range(1,n):
        if n  % i == 0:
            count +=1
    if count < 2:
       return True


def main():
    print("Enter the size of list : ")
    size = int(input())
    print("Enter list : ")
    Data = []
    for i in range(size):
        Data.append(int(input()))

    ret = list(filter(checkPrime,Data))
    print(ret)

if __name__ == "__main__":
    main()