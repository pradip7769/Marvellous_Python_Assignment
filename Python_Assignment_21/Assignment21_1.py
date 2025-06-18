# Q1. Design automation script which display information of runnig process as its name, PID, Username. 
# Using : ProcInfo.py

import psutil

def ProcInfo():
    for proc in psutil.process_iter(['pid','name','username']):
        print(f"Process Name: {proc.info['name']}, PID: {proc.info['pid']}, Username: {proc.info['username']}")
        # print(proc)


def main():
    ProcInfo()

if __name__ == "__main__":
    main()