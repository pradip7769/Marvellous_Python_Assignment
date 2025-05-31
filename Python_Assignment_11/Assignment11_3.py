#Q3 Sum of Digits
# Write a recursive function to calculate the sum of digits of a number.
# SUM of digitas(1234) --> 10

sum = 0
digit = 0
def sum_of_digit(no):
    global sum 
    global digit
    if no >= 1:
        digit = no % 10
        sum += digit
        sum_of_digit(no // 10)
    return sum


def main():
   print("Enter the n number : ")
   no = int(input())
   SUM = sum_of_digit(no)
   print("sum_of_digit is : ", SUM)

if __name__ == "__main__":
    main()