#Q3 Accept a number from the user and print its multiplication table up to 10.
# Expected Input : 7
# Expected Ouput 
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

def printTable(n):
    for i in range(1, 11):
        print(n,"x",i,"=",n*i)


def main():
    print("Enter a number : ")
    num = int(input())
    printTable(num)

if __name__ == "__main__":
    main()







