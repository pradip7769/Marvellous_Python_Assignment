# Q1. Design automation script which accept directory name and file extension from user. Display all files with that extension.
# Usage : DirectoryFileSearch.py "Demo" ".txt"
# Demo is a name of directory and .txt is the extension that we want to search. 

import os 
import sys

def DirectoryFileSearch():
    DirectoryName = os.path.abspath(sys.argv[1])
    ExtensionName = sys.argv[2]

    flag = os.path.isabs(DirectoryName)

    if(flag == False):
       
        DirectoryName = os.path.abspath(DirectoryName)
    
    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("There is no such directory")
        exit() 
    
    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("path is valid but the target is not a directory")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):    
        for fname in FileNames:  
            if fname.endswith(ExtensionName):
                fname = os.path.join(FolderName,fname)
                print(fname)



def main():
    DirectoryFileSearch()
    

if __name__ == "__main__":
    main()

