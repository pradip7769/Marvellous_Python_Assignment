#Q5 Write a program which contains filter(), map() and reduce() in it. Python application which
# Contains one list of numbers. List contains the numbers whcih are accepted form user. Filter should filter out
# all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers.
# (You can also use normal functions instead of lambda funcitons).

# Input List = [2,70,11,10,17,23,31,77]
# List after filter = [2,11,17,23,31]
# List after map = [4,22,34,46,62]
# Output of reduce = 62

from functools import reduce

def CheckPrime(Data):
    result = []
    count = 0
    for i in range(1,Data):
        if Data % i == 0:
                count += 1
    if count < 2:
          result.append(Data)
    return result

def multi(Data):
     return Data * 2

def maximum(value1,value2):
     max = value1
     if value2 > max:
        max =  value2
     return max


def main():
    print("Enter the size of list : ", end="")
    size_of_list = int(input())
    print("Enter the list elements : ")
    Data = []

    for i in range(size_of_list):
        no = int(input())
        Data.append(no)
    print("Data : ", Data)
    FData = list(filter(CheckPrime,Data))
    print("FData : ", FData)
    MData = list(map(multi,FData))
    print("MData : ", MData)
    RData = reduce(maximum,MData)
    print("RData : ", RData)

if __name__ == "__main__":
    main()