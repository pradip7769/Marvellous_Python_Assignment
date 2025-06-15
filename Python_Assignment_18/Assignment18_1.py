# Q1. Write a program which accepts file name from user and check whether that file exists in current directory or not.
# Input : Demo.txt
# Check Whether Demo.txt exists or not.

import os 

def main():
    print("Enter the FileName : ", end=" ")
    FileName = input()

    exist =  os.path.exists(FileName)
    if exist:
        print("File is exist in current directory...")
    else:
        print("File does not exist in current directory...")

if __name__ == "__main__":
    main()