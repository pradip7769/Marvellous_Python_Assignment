
def CheckWhether(no):

    if (no == 0):
        print("number is Zero")
    elif (no > 0):
        print("Positive Number")
    else:
        print("Negative Number")

def main():
    print("Enter the number : ")
    num = int(input())

    CheckWhether(num)

if __name__ == "__main__":
    main()

        
        

