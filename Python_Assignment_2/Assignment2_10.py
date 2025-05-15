
def add_digit(digit):
    sum = 0
    for x in range(len(digit)):
        sum = sum + int(digit[x])
    
    return sum



def main():
    print("Enter the Pattern No : ")
    # value = int(input())
    value = input()
    ret = add_digit(value)
    print("Addition is : ", ret)

if __name__ == "__main__":
    main()