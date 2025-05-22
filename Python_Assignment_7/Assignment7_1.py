#Q1 Write two lambda functions: 
# 1. Calculate square of a number
# 2. Another to calculate cube of a number
# Expected Input : Enter a number : 3
# Expected Output : Square : 9  Cube 27

square = lambda x : x * x
cube = lambda x : x * x * x

def main():
    print("Enter a number : ",end="")
    num = int(input())
    squ = square(num)
    cub = cube(num)
    print("Square : ",squ)
    print("Cube : ",cub)

if __name__ == "__main__":
    main()
