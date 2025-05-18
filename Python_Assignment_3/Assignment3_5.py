
from MarvellousNum import chkPrime

def ListPrime():
    print("Enter the N number of elements : ")
    N = int(input())

    numbers=[]
    i = 0
    print("Enter the",N,"Elements : ")

    while i < N:
        numbers.append(int(input()))
        i+=1
    
    ret = chkPrime(value= numbers)
    print("Output : ", ret)


def main():
   ListPrime()


if __name__ == "__main__":
    main()
