power = lambda value : value * value

def main():
  
    print("Enter the number : ")
    num = int(input())
    ret = power(num)
    print("Power is : ", ret)

if __name__ == "__main__":
    main()