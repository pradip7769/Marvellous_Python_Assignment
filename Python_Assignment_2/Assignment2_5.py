
def CheckPrime(checkNO):

    if(checkNO % 2 != 0):
        print(checkNO,"is a Prime Number")
    else:
        print(checkNO,"is not a Prime Number")

def main():
    print("Enter the Check Prime Number : ")
    value = int(input())
    CheckPrime(value)

if __name__ == "__main__":
    main()