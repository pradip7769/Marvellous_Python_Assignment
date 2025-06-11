# Write a Program which accepts file name from user and check whether that file exists in current directory or not. 
# Input : Demo.txt
# Check whether Demo.txt exists or not.
import os 

def checkWhether(file):
    ret = os.path.exists(file)
    if ret == True:
        print("File is exists in current directory")
    else:
        print("File is does not exists in current directory")


def main():
    print("Enter the File Name : ")
    FileName = input()
    checkWhether(FileName)


if __name__ == "__main__":
    main()