# Write a program to read and display the contents of a file data.txt.

import sys 
import os 

def ReadContent():
    FileName = sys.argv[1]
    exist = os.path.exists(FileName)

    if exist == True:
        myFile = open(FileName,"r")
        content = myFile.read()
        print("File Content : ")
        print(content)
        myFile.close()
    else:
        print("File is not exist in current directory")

def main():

     if len(sys.argv) == 2: 
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to read the file data and display the contents")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("python File_Name.py data.txt")
     else:
         print("Incorrect Input parameter received.")
         print("Use '--h' for help or '--u' for how to use")

     ReadContent()


if __name__ == "__main__":
    main()