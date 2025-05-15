
def printAstrik(Astric):

    for x in range(Astric):
        for y in range(Astric):
            print("*", end=" ")
        print("")


def main():

    print("Ennter the count number of '*' : ")
    count = int(input())
    printAstrik(count)

if __name__ == "__main__":
    main()