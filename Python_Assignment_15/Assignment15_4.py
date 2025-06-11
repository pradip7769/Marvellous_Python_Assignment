# Write a program which accept two file names from user and compare contents of both the files. 
# If both the files contains same contents then display success otherwise display failure. 
# Accept names of both the files from command line. 

# Input : Demo.txt  Hello.txt
# compare contents of Demo.txt and Hello.txt 

import sys 
import os 

def compareContents(file1, file2):

    
        check1 = os.path.exists(file1)
        check2 = os.path.exists(file2)

        if check1 == True and check2 == True:
            src1 = open(file1,"r")
            src2 = open(file2,"r")

            content1 = src1.read()
            content2 = src2.read()

            if content1 == content2:
                print("Success")
            else:
                print("Failure")
            src1.close()
            src2.close()
        else:
            print("Fiel does not exists")
    



def main():

    if len(sys.argv) == 3: 
         file1 = sys.argv[1]
         file2 = sys.argv[2]
         compareContents(file1,file2)
    else:
         print("Wrong file name is received")

if __name__ == "__main__":
    main()