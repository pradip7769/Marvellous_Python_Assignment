# Write a program which accept file name from user and open that file and display the contents of that file on screen.
# Input : Demo.txt 
# Display Contents of Demo.txt on console. 

import os 

def readContents(FileName):

    ret = os.path.exists(FileName)
    if ret == True:
        file = open(FileName,"r")
        print(file.read())
        file.close()
    else:
        print("File is does not exists in current directory")

def main():
    print("Enter the file name : ")
    FileName = input()
    readContents(FileName)

if __name__ == "__main__":
    main()