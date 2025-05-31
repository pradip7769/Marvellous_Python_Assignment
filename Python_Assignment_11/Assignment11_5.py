# Count Zeros in a Number (Recursively)
# Write a recursive function to count how many zeros are in the given number.
# coutn_Zeros(1020300) --> 4 

count = 0
check = 0

def count_zeros(n):
    global count
    global check
    if n >= 1:
      check = n % 10
      n = n // 10
      if (check == 0):
           count +=1
      count_zeros(n)
      return count
      

def main():
   print("Enter the num & power value : ")
   no1 = int(input())

   ret = count_zeros(no1)
   print("count_zero is : ", ret)

if __name__ == "__main__":
    main()