# Q1. Design automation script which accept directory name and delete all duplicate files form that directory. 
# Write names of duplicate files from that directory into log file named as Log.txt. 
# log.txt file should be created into current directory.

# Usage : DirectoryDuplicateRemoval.py "Demo"
# Demo is name of directory.

import os 
import sys 
import time
import hashlib

Border = "_"*78

def CalculateCheckSum(path , BlockSize = 1024):
    
    fobj = open(path,"rb")

    hobj = hashlib.md5()
    
    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)
    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(DirectoryName = "Marvellous"): 

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

    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):    
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateCheckSum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]

    return Duplicate

def deleteDuplicate(Path = "Marvellous"):

    MyDict = FindDuplicate(Path)
    Result = list(filter(lambda x : len(x) > 1,MyDict.values()))
    
    count = 0
    cnt = 0
    for Value in Result:
        for subvalue in Value:
            count += 1
            if (count > 1):
                 print("Deleted file : ", subvalue)
                 os.remove(subvalue)
                 cnt += 1
        count = 0
    print("Total deleted file : ", cnt)
           
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
            print("ScriptName.py NameOfDirectory timeInterval")
            print("Please provide valid absolute path")
        
        else:
            deleteDuplicate(sys.argv[1])


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