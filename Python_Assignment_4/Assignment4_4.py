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