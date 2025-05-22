#Q4. Find Largest Among Three Numbers
# Accept three numbers from the user and print the largest using nested if-else statements.
# Expected Input: Enter three numbers : 5, 9,3
# Expected Output : Largest number is 9
def findLargest(no):
    large = no[0]
    for i in no:
        if i >= large:
            large = i
    return large
    
def main():
    print("Enter the three number : ")
    num = []
    for i in range(3):
        num.append(int(input()))
    
    ret =  findLargest(num)
    print("Largest Number : ", ret)
   

if __name__ == "__main__":
    main()
