# Q2 Write a program which contains one lambda function which accepts two parameters and return its multiplication
# Input : 4 * 3    Output : 12
# Input : 6 * 3    Output : 18

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