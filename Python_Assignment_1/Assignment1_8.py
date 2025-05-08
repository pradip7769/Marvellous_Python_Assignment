
def star(no):
    i = 0
    while i < no:
        print("*")
        i = i + 1

def main():
    print("Enter the printing value of star : ")
    num = int(input())
    star(num)

if __name__ == "__main__":
    main()