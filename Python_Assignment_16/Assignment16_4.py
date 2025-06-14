# Q4. Accept 10 numbers from the user and write them into a file named numbers.txt, each on a new line.

import os 
import sys 

def writeNumbers():
    FileName = sys.argv[1] 
    
    if FileName != "--h" and FileName != "--H" and FileName != "--u" and FileName != "--U":
        exists = os.path.exists(FileName)
        if exists == True:
            myFile = open(FileName,"w")
            print("Enter the Number length you want to write in file : ")
            length = int(input())
            print("Enter the", length ,"Numbrs to store in File : ")
            for i in range(length):
                myFile.write(input())
                myFile.write("\n")
            myFile.close()
            print("Numbers write and File closed Successfully")
        else:
            print("File is not exists in current directory")

def main():
      if len(sys.argv) == 2: 
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to read the file data and display the contents")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("python File_Name.py example.txt")
      else:
         print("Incorrect Input parameter received.")
         print("Use '--h' for help or '--u' for how to use")

      writeNumbers()


if __name__ == "__main__":
    main()