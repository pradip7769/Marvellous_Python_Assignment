# Q4 Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.

# Input List = [5,2,3,4,3,4,1,2,8,10]
# List after filter = [2,4,4,2,8,10]
# List after map = [4,16,16,4,64,100]
# Output of reduce = 204

import functools

def CheckEven(Data):
    result = []
    if Data % 2 == 0:
        result.append(Data)
    return result

def square(Data):
    return Data * Data

def sum(value1, value2):
    return value1 + value2

def main():
    print("Enter the size of list : ", end="")
    size_of_list = int(input())
    Data = []
    print("Enter the list Element : ")

    for i in range(size_of_list):
        no = int(input())
        Data.append(no)
    
    print("Data : ", Data)
    FData = list(filter(CheckEven,Data))
    print("FData : ", FData)
    MData = list(map(square,FData))
    print("MData : ", MData)
    RData = functools.reduce(sum,MData)
    print("RData : ", RData)
    

if __name__ == "__main__":
    main()