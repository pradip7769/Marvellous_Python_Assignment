# Q1. Write a program which accept file name from user and open that file and display the contents of that file on screen. 
# Input : Demo.txt
# Display contents of Demo.txt on console.

import os 

def main():
    print("Enter the FileName : ", end=" ")
    FileName = input()

    exist =  os.path.exists(FileName)
    if exist:
        print("File is exist in current directory...")
        myFile = open(FileName,"r")
        content = myFile.read()
        print(content)
        myFile.close()

    else:
        print("File does not exist in current directory...")

if __name__ == "__main__":
    main()