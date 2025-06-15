# Q1. Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. 
# Accept file name through command line arguments.

# Input : ABC.txt
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

import os 
import sys 

def copyContent():

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    exist = os.path.exists(File1)
    if exist:
        print("File exist in current Directory")

        myFile1 = open(File1,"r")
        myFile2 = open(File2,"w")

        content = myFile1.read()
        myFile2.write(content)

        myFile1.close()
        myFile2.close()
        print("Copy Content Successfully...")
    
    else:
        print("File is not exist in current directory")

def main():
    print("-" * 58)

    if(len(sys.argv) == 3):
        if((sys.argv[1] == "-h") or (sys.argv[1] == "-H")):
            print("This application is used to perform Directory cleaning")
            print("This is directory automation Script...")
        
        elif((sys.argv[1] == "-u") or (sys.argv[1] == "-U")):
            print("Use the given script as : ")
            print("ScriptName.py ABC.txt Demo.txt")
            print("ABC.txt to Copy the content and Write in Demo.txt")
            print("Please provide valid absolute path")
        
        else:
            copyContent()

    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flag as : ")
        print("--h : used to display the help")
        print("--u : Used to display the usage")

    print("-" * 58)
    print("--------------Thank you for using our script--------------")
    print("-" * 58)

if __name__ == "__main__":
    main()