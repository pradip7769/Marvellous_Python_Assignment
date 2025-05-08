
def Add(no1, no2):
    sum = no1 + no2
    return sum

def main():

    print("Enter the First number : ")
    num1 = int(input())
    print("Enter the Second number : ")
    num2 = int(input())
    
    add = Add(num1,num2)

    print("Addition is : ", add)


if __name__ == "__main__":
    main()