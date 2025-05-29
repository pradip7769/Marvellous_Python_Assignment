#Write a program which contains one lambda function which accepts one parameter and return power of two
# Input : 4  Output : 16
# Input : 6  Output : 64

power = lambda value : value * value

def main():
  
    print("Enter the number : ")
    num = int(input())
    ret = power(num)
    print("Power is : ", ret)

if __name__ == "__main__":
    main()