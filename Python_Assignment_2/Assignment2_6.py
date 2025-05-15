
def printAstric(Astric):
    
    for x in range(Astric,0,-1):
        for y in range(x):
            print("*", end=" ")
        print("")
    
    
def main():
    print("Enter the size of reverse Astric : ")
    value = int(input())
    printAstric(value)

if __name__ == "__main__":
    main()