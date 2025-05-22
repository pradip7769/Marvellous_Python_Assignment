# Q5. Write a function that accepts a string and checks whether it is a palindrome.
# Expected Input: Enter a string: radar
# Expected Output : radar is a palindrome.


def reverse(String):
    #  print(String)
     length = len(String) - 1
     i = 0
     rev = ""
     while length >= i:
        #  print(String[length])
         rev += String[length]
         length -= 1

     print(rev)
     if rev == String:
        print(String,"is palindrome.")
     else:
        print(String,"is not Palindrome")
  
def main():
    print("Enter a string: ")
    name = input()
    reverse(name)

if __name__ == "__main__":
    main()