# Q2. Design automation script which accept process name and display information of that process if it is running. 
# Usge : ProceInfo.py Notepad 

import psutil 
import sys 


def CheckProcisRunning():
    ProcessName = sys.argv[1]


    for proc in psutil.process_iter(['name']):
        # print(proc.info['name'])
        if proc.info['name'] == ProcessName:
            print(f"{proc.info['name']} Process is is running")
       
def main():
    CheckProcisRunning()

if __name__ == "__main__":
    main()