# Q5. Write a Program to read a file line by line and display only those lines that contain more than 5 words. 


import sys 
import os 

def redFile():
    FileName = sys.argv[1]
    exist = os.path.exists(FileName)

    if exist == True:
        print("File exist in current directory")
        myFile = open(FileName,"r")

        content = myFile.readlines()
        
        for line in content:
           count = 0
           for char in line:
               if char == ' ':
                   count +=1
           if(count >= 5):
               print(line)
    else:
        print("File is not exist in current directory")
            

def main():
    if len(sys.argv) == 2: 
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to read the file data and display the contents")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("python File_Name.py example.txt")
    else:
         print("Incorrect Input parameter received.")
         print("Use '--h' for help or '--u' for how to use")

    redFile()


if __name__ == "__main__":
    main()