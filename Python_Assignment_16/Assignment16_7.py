# Q7. Create a file marks.txt with student name and marks. Then read the file and display students who scored more than 75 marks.

import sys 
import os 

FileName = sys.argv[1]

def createFile():

    exist = os.path.exists(FileName)

    if exist == True:
        print("File is already exist")
    else:
        myFile = open(FileName,"w")
        myFile.close()
        print("File Created successfull")

def Std_Namd_Marks():

    exist = os.path.exists(FileName)
    print("Enter the lenght of student list : ")
    length = int(input())
    if exist == True:
        print("Enter the student Name and Marks : ")
        myFile = open(FileName,"w")
        for i in range(length):
            stdName = input()
            stdMarks = input()
            myFile.write(stdName + ":" + stdMarks + "\n")
        myFile.close()
        print("Student Name and Marks Written Successfully...")
    else:
        print("File is not exist in current directory")

def checkScored():
    exist = os.path.exists(FileName)
    if exist:
        print("File exists in current directory")
        myFile = open(FileName, "r")
        content = myFile.readlines()  # read lines instead of the whole content

        for line in content:
            line = line.strip()
            if ':' in line:
                name, mark = line.split(":")
                if int(mark) > 75:
                    print(f"{name} has marks greater than 75: {mark}")
        myFile.close()
    else:
        print("File does not exist")

def main():

    if len(sys.argv) == 2: 
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to read the file data and display the contents")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("python File_Name.py example.txt")
    else:
         print("Incorrect Input parameter received.")
         print("Use '--h' for help or '--u' for how to use")

    createFile()
    Std_Namd_Marks()
    checkScored()


if __name__ == "__main__":
    main()