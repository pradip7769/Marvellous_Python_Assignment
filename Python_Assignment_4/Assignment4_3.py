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

