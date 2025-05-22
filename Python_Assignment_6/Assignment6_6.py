#Q6. Print Triangle Pattern using Nested Loops
# Expected Output : 
# *
# * *
# * * *
# * * * *

def main():

    for i in range(5):
        for j in range(i):
            print("*",end=" ")
        print()
        

if __name__ == "__main__":
    main()