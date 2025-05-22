#Q7 Accept 5 numbers from the user. Find and print the largesr number.
# Expected input : Enter 5 numbers : 23 89 12 56 45
#Expected Output : Maximum number is : 89


def Max(n):
    value = n[0]
    for i in n:
        if i > value:
            value = i
    return value



def main():
    print("Enter 5 number : ")
    number = []
    for i in range(5):
        number.append(int(input()))
    
    max = Max(number)
    print("Maximum number is : ", max)

if __name__ == "__main__":
    main()