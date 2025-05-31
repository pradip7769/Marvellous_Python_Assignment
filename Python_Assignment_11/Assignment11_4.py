# Power Function Using Recursion
# Write a recursive function to caluculate x ^ n.
# power(2,3) --> 8

result = 1
def power(no,p):
    global result
    if(p >= 1):
        result = result * no
        power(no,p-1)
    return result


def main():
   print("Enter the num & power value : ")
   no1 = int(input())
   no2 = int(input())

   ret = power(no1,no2)
   print("power is : ", ret)

if __name__ == "__main__":
    main()