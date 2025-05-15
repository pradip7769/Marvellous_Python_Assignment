
import Arithmetic

def main(): 
    print("Choose the Calculation Method : ")
    print("1.Add \n2.Sub \n3.Mul \n4.Div")
    caluculator = int(input())

    if(caluculator < 5):
        print("Eneter the first value : ")
        value1 = int(input())
        print("Enter the second value : ")
        value2 = int(input())

    if (caluculator == 1):
        Arithmetic.Add(value1,value2)
    elif (caluculator == 2):
        Arithmetic.Sub(value1,value2)
    elif (caluculator == 3):
        Arithmetic.Mult(value1,value2)
    elif (caluculator == 4):
        Arithmetic.Div(value1,value2)
    else:
        print("Choose the correct keyword...")


if __name__ == "__main__":
    main()

