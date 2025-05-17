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