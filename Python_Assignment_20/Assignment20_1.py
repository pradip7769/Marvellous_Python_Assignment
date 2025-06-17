# Q1. Desing Automation Script which accept directory name and display checksum of all files. 
# Usage : DirectoryChecksum.py "Demo"
# Demo is name of directory.

import os 
import sys 
import hashlib

Border = "_"*78

def CalculateCheckSum(path, BlockSize = 1024):
    fobj = open(path,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)
    
    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):
    flag = os.path.abspath(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("There is no such directory")
        exit()
    
    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName, subFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            full_path = os.path.join(FolderName, fname)
            checksum = CalculateCheckSum(full_path)
            print("File Name : ", fname)
            print("Checksum : ", checksum)
            print("\n")

def main():
    print(Border)
    print("------------------------- Marvellous Automation ------------------------------")
    print(Border)

    if (len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform Directory cleaning")
            print("This is directory automation Script...")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as : ")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid absolute path")

        else:
            DirectoryWatcher(sys.argv[1])
    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flag as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

    print(Border)    
    print("-------------------- Thank you for using our script --------------------------")
    print("------------------------- Marvellous Infosystem  -----------------------------")
    print(Border)

if __name__ == "__main__":
    main()