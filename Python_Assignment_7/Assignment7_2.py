# Q2. Accept a list of integers from the user and use the map() function to double each value.
# Expected Input : Enter list : 1 2 3 4 5 
# Expected Ouput : [2,4,6,8,10]


double = lambda x : x + x

def main():
    print("Enter the size of list : ")
    size = int(input())
    print("Enter the list elements  :")
    Data = []
    for i in range(size):
        Data.append(int(input()))
    
    ret = list(map(double,Data))

    print(ret)

if __name__ == "__main__":
    main()