def common(List,No):

    i = 0
    for x in List:
        if x == No:
            i+=1
    return i

def main():
    print("Enter the N number of elements : ")
    N = int(input())

    numbers=[]
    i = 0
    print("Enter the",N,"Elements : ")

    while i < N:
        numbers.append(int(input()))
        i+=1
    
    print("Enter the Searching element : ")
    no = int(input())
    ret = common(List= numbers,No = no)

    print("Output : ", ret)


if __name__ == "__main__":
    main()