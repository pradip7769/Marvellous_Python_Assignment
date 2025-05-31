# Q7 Print Pattern Using Recursion (Right Triangle)
# Write a recursive function to print the following patter : 

# *
# * *
# * * *
# * * *  * 


def patter(n):
    if n >= 1:
        patter(n -1)
        for i in range(n):
            print("*",end=" ")
        print()
        

def main():
   print("Enter the pattern number : ")
   no = int(input())
   patter(no)

if __name__ == "__main__":
    main()