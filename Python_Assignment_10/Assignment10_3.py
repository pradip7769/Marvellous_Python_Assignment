#Q3 Write a program which contains filter(), map() and reduce() in it. Python applicaiton which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# Should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List = [4,34,36,76,68,24,89,23,89,90,45,70]
# List after filter = [76,89,86,90,70]
# List after map = [86,99,96,100,80]
# Output of reduce = 6538752000

from functools import reduce

def greaterNO(Data):
    retLIST = []
    if Data >= 70 and Data <= 90:
        retLIST.append(Data)
    return retLIST

def increaseNO(Data):
    return Data + 10

def multi(value1,value2):
    return value1 * value2

def main():
    print("Enter the size of list : ",end="")
    size_of_list = int(input())
    Data = []
    print("Enter the list element : ")

    for i in range(size_of_list):
        no = int(input())
        Data.append(no)
    
    print("Data: ", Data)
    FData = list(filter(greaterNO,Data))
    print("FData : ", FData)
    MData = list(map(increaseNO,FData))
    print("MData : ", MData)
    RData = reduce(multi,MData)
    print("RData : ", RData)

if __name__ == "__main__":
    main()

