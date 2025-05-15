
def add_digit(digit):
    no_digit = 0
    x = 0
    while x <= len(digit):
        no_digit = x
        x+=1
    
    return no_digit


def main():
    print("Enter the Pattern No : ")
    # value = int(input())
    value = input()
    ret = add_digit(value)
    print("Addition is : ", ret)

if __name__ == "__main__":
    main()