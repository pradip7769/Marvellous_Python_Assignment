
def sum_of_list(List):
    sum = 0
    i = 0
    while i < len(List):
        sum += List[i]
        i+=1
   
    return sum



def main():
    print("Enter the N number of value : ")
    N = int(input())
    element = []

    print("enter the",N,"Values")

    for x in range(N):
        element.append(int(input())) 

    add = sum_of_list(element)
    print("Addition is : ", add)
    

if __name__ == "__main__":
    main()