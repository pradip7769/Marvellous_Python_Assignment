
def fun(no):

    result  = no % 5

    if(result == 0):
        return True
    else:
        return False

def main():
    print("Enter the value")
    num = int(input())
    answer = fun(num)
    print(answer)

if __name__ == "__main__":
    main()
