
def checkMinimum(List):
    check = List[0]
    for x in List:  
        if check > x:
            check = x
        
    return check
            

def main():
    print("Enter the N number : ")
    N = int(input())
    numbers = []

    i = 0
    print("Enter",N,"Value : ")
    while i < N:
        numbers.append(int(input()))
        i+=1
    
    ret = checkMinimum(numbers)
    print("Minimum value is : ", ret)


if __name__ == "__main__":
    main()
