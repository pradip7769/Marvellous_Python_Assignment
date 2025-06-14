# Q7. Schedule a function that performs file backup every hour and writes a log entry into backup_log.txt


import schedule
import time
import os
import shutil
from datetime import datetime

# Configuration
SOURCE_FILE = "data.txt"  # File you want to back up (must exist in same dir as script or provide full path)
BACKUP_DIR = r"C:\Users\pradi\Desktop\Python_Assignment\Python_Assignment_17"
LOG_FILE = "backup_log.txt"

def checkdir():
    try:
        os.makedirs(BACKUP_DIR,exist_ok=True)
    except:
        print("Directory is not exixst : ")


def perform_backup():

    Time = time.localtime()
    Time = time.strftime("%H_%M_%S",Time)
    # print("Backup Time : ", Time)

    backup_filename = "Backup_" + Time + ".txt"
    print(backup_filename)

    src_exist = os.path.exists(SOURCE_FILE)
    log_exist = os.path.exists(LOG_FILE)

    if log_exist != True:
        log_File = open(LOG_FILE,"w")
        log_File.close()
    
    if src_exist == True:

        src_File = open(SOURCE_FILE,"r")
        dst_File = open(backup_filename,"w")
        log_File = open(LOG_FILE,"a")
        content = src_File.read()
        dst_File.write(content)
        log_File.write("Backup Time : " + Time + "\n")

        src_File.close()
        dst_File.close()
        log_File.close()

def main():

    schedule.every().minutes.do(perform_backup)
    print("Backup scheduler started. Running every hour...")
    checkdir()

    # Run scheduler loop
    while True:
        schedule.run_pending()
        time.sleep(1)
   

if __name__ == "__main__":
    main()