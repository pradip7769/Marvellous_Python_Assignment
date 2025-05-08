
def even_NO(no):
    
    i = 1
    while i <= no:

        result = i % 2

        if(result == 0):
            print(i, end=" ")

        i = i + 1

           

def main():
    print("Enter the value of check even no : ")
    num = int(input())
    even_NO(num)

if __name__ == "__main__":
    main()