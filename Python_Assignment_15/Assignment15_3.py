# Write a program which accept file name from user and create new file named as Demo.txt
# and copy all contnts from existing file in new file.
# Accept file name through command line arguments. 

# Input : ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

import sys 
import os 


def CopyContents():

    if len(sys.argv) == 2:
        ret = os.path.exists(sys.argv[1])
        if ret == True:
            src = open(sys.argv[1],"r")
            dst = open("Demo.txt","w")

            contents = src.read()
            dst.write(contents)

            src.close()
            dst.close()
        else:
            print("File is does not exists in current directory...")
    else:
        print("wrong input is received")


def main():
   CopyContents()

if __name__ == "__main__":
    main()