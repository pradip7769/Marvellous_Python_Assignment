# Q3 Write a Python script to count the number of lines, words, and characters in a given file. 

import sys 
import os 

def count():
    FileName = sys.argv[1]

    try:
        myFile = open(FileName,"r")
        myFile = myFile.readlines()
        numLines = 0 
        numWords = 0 
        numChar = 0 

        for line in myFile:
            numLines +=1 
            for char in line:
                numChar+= 1
            line = line.strip().split()
            for words in line:
                    numWords += 1 
        
        print(numLines)
        print(numWords)
        print(numChar)

    except FileNotFoundError:
        print("File is does not exist in current direcotry")

def main():
    if len(sys.argv) == 2: 
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to read the file data and display the contents")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("python File_Name.py example.txt")
    else:
         print("Incorrect Input parameter received.")
         print("Use '--h' for help or '--u' for how to use")

    count()


if __name__ == "__main__":
    main()