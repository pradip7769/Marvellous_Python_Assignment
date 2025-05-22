# Q2. Vowel or Consonant Check
# Accept a single character from the user and check if it is a vowel (a,e,i,o,u). if not, print it's consonant.
# Expected input : Enter a character : e
# Expected Output : 'e' is a vowel

def checkVovels(vovel):
    if vovel == 'a' or vovel == 'e' or vovel == 'i' or vovel == 'o' or vovel == 'u':
        print(vovel , "is vovel ")
    else:
        print(vovel, "is consonant")

def main():
    print("enter a character : ", end="")
    vovel = input()
    checkVovels(vovel)


if __name__ == "__main__":
    main()


    
    