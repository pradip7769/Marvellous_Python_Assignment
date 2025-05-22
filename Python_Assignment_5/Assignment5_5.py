#Q5. Even or Odd Number Check
# Write a program to check whether the entered number is even or odd
# Expected Input : Enter a number : 17 
# Expected Output : 17 is an odd number

Even = lambda num : num % 2 == 0

def checkEven(Task,value):
    if Task(value):
        print(value,"is Even")
    else:
        print(value,"is Odd")

def main():
    print("Enter the Even or Odd num : ", end="")
    num = int(input())
    checkEven(Even,num)

if __name__ == "__main__":
    main()
