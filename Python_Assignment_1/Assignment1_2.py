

def ChkNum(no):
    check_no = no % 2

    if(check_no == 0):
        print("Even Number...")
    else:
        print("Odd Number...")

def main():
    print("Enter the Check Even or Odd Number : ")

    num = int(input())
    ChkNum(num)



if __name__ == "__main__":
    main()
