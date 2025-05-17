power = lambda value1,value2 : value1 * value2

def main():
  
    print("Enter the first value : ")
    num1 = int(input())
    print("Enter the second value : ")
    num2 = int(input())
    ret = power(num1,num2)
    print("Power is : ", ret)

if __name__ == "__main__":
    main()