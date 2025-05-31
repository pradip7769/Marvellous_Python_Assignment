#Q1. Print Numbers Using Recursion
# Write a recursive function to print numbers from 1 to N
# Expected output (for n = 5):
# 1 2 3 4 5

def recursive(n):
    if(n > 0):
        recursive(n-1)
        print(n,end=" ")   
       
def main():
   print("Enter the n number : ")
   no = int(input())
   recursive(no)

if __name__ == "__main__":
    main()