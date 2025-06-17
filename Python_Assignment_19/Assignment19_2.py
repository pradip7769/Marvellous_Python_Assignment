# Q2. Design automation script which accept directory name and two file extensions from user. 
# Rename all files with first file extension with the second file extenntion. 
# Usage : DirecotryRename.py "Demo" ".txt" ".doc"

# Demo is name of directory and .txt is the extension that we want to search and rename with .doc. 
# After execution this script each .txt file gets renamed as .doc. 


import os 
import sys
from pathlib import Path

def DirectoryFileSearch():
    DirectoryName = os.path.abspath(sys.argv[1])
    ExtensionName1 = sys.argv[2]
    ExtensionName2 = sys.argv[3]

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
            if fname.endswith(ExtensionName1):
                fname = os.path.join(FolderName, fname)
                file_path = Path(fname)
                new_file = file_path.with_suffix(ExtensionName2)
                file_path.rename(new_file)


def main():
    DirectoryFileSearch()
    

if __name__ == "__main__":
    main()

