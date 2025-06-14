# Q8. Write a script to remove all blank lines from a file. Save the cleaned output to a new file. 

import sys 
import os 

newFileName = "newFile.txt"

def removeBlank():
    FileName = sys.argv[1] 
    print("FileName : ", FileName)

    try:
        exist = os.path.exists(FileName)
        if exist:
            myFile = open(FileName,"r")
            content = myFile.readlines()
            newFile = open(newFileName,"w")
            for line in content:
                
                line = line.strip()
                if line:
                    newFile.write(line)
                    newFile.write("\n")

            myFile.close()
            newFile.close()

        else:
            print("File is not exist in current directory")

    except FileNotFoundError:
        print("File is not found in current directory")



def main():
    if len(sys.argv) == 2: 
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to read the file data and display the contents")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("python File_Name.py example.txt")
    else:
         print("Incorrect Input parameter received.")
         print("Use '--h' for help or '--u' for how to use")

    removeBlank()


if __name__ == "__main__":
    main()