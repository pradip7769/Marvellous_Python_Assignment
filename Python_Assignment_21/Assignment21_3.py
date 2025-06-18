# Q3. Design automation script which accept directory name form user and create log file in that 
# directory which contains information of running processes as its name, PID, Username. 

# Usage ProcInfoLog.py Demo 

# Demo is name of Direcotry.

import psutil 
import sys 
import os 
import time 

def ProcInfoLog():
    DirName = sys.argv[1]
    if not os.path.exists(DirName):
        os.makedirs(DirName)
    
    Time = time.ctime()
    FileName =  Time + ".txt"
    FileName = FileName.replace(":","_")
    FileName = FileName.replace(" ","_")
    print(FileName)
    FilePath = os.path.join(DirName,FileName)
    
    myFile = open(FilePath,"w")

    for proc in psutil.process_iter(['pid','name','username']):
        myFile.write(f"Process Name: {proc.info['name']}, PID: {proc.info['pid']}, Username: {proc.info['username']}")
        myFile.write("\n")

    myFile.close()


def main():
    ProcInfoLog()

if __name__ == "__main__":
    main()