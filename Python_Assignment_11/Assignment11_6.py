# Sum of First N Natural Numbers
# Write a recursive function to calculate sum from 1 to n.
# sum_n(5)  --> 15

sum = 0
def sum_n(n):
    global sum
    if n >= 1:
        sum += n
        sum_n(n - 1)
    return sum

def main():
   print("Enter the n number : ")
   no = int(input())
   SUM = sum_n(no)
   print("sumof number is : ", SUM)

if __name__ == "__main__":
    main()