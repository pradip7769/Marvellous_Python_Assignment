
def checkMaxixmum(List):
    check = 0
    for x in List:
        if check < x:
            check = x
        
    return check
            


def main():
    print("Enter the N number : ")
    N = int(input())

    numbers = []
    i = 0
    print("Enter ",N,"numbers : ")
    while i < N:
        numbers.append(int(input()))
        i+=1
    
    Max = checkMaxixmum(numbers)
    print("Maximum Number is : ", Max)

if __name__ == "__main__":
    main()
