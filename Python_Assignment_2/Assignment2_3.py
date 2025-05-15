
def factorial(fact_value):

    fact = 1
    for x in range(1,fact_value + 1):
        fact = fact * x
    
    print("factorial number is : ", fact)

def main():
    print("Enter the factorial number : ")
    value = int(input())
    factorial(value)

if __name__ == "__main__":
    main()