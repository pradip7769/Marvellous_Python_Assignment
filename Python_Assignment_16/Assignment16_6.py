# Q6. Write a Python program to copy the contents of one file (source.txt) into another file (destination.txt)

import sys 
import os 

def copyContent():

    src_FileName = sys.argv[1] 
    dst_FileName = sys.argv[2]
    
    if src_FileName != "--h" and src_FileName != "--H" and src_FileName != "--u" and src_FileName != "--U":

        source_exist = os.path.exists(src_FileName)
        desti_exist = os.path.exists(dst_FileName)

        if source_exist == True and desti_exist == True:
            src_File = open(src_FileName,"r")
            dst_File = open(dst_FileName,"w")

            content = src_File.read()
            dst_File.write(content)
            src_File.close()
            dst_File.close()
            print("Content Copy and File close succesfull")
        else:
            print("File is not exists in current directoy")

def main():

    if (len(sys.argv) == 3):
        copyContent()
        exit()

    if len(sys.argv) == 2: 
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This program is used to copy the contents in source.txt to pase destination.txt file")
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("python File_Name.py source.txt destination.txt")
    else:
         print("Incorrect Input parameter received.")
         print("Use '--h' for help or '--u' for how to use")

if __name__ == "__main__":
    main()