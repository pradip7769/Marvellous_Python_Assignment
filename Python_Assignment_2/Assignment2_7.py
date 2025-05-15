
def pattern(no):

    i = 1
    while i <= no:
        j = 1
        while j <= no:
            print(j,end=" ")
            j = j+ 1 
        print("")
        i = i + 1

def main():
    print("Enter the Pattern No : ")
    value = int(input())
    pattern(value)

if __name__ == "__main__":
    main()