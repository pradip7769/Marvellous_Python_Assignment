
def sum_of_fact(fact_value):
    sum = 0
    i = 1
    while i < fact_value:
        if(fact_value % i == 0):
            sum += i
        i+=1
    return sum

def main():
    print("Enter the Addition of Factor Number : ")
    value = int(input())
    fact = sum_of_fact(value)
    print("Sum of fact : ", fact)

if __name__ == "__main__":
    main()