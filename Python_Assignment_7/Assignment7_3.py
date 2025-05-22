# Q3. Accept a list of numbers and use filter() to keep only even numbers. 
# Expected Input: Enter list : 1 2 3 45 6
# Expected Output : Even numbers: [2,4,6]

even = lambda x : x % 2 == 0

def main():
    print("Enter the size of list : ")
    size = int(input())
    print("Enter list : ")
    Data = []
    for i in range(size):
        Data.append(int(input()))

    ret = list(filter(even,Data))
    print(ret)

if __name__ == "__main__":
    main()