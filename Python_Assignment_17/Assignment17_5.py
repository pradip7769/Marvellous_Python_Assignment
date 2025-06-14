# Q4. Schedule a job that runs every 5 Minutes to write the current time to a file Marvellous.txt.


import schedule 
import time 
import os

def WriteTime():
    FileName = "Marvellous.txt"
    Time =  time.localtime()
    Time = time.strftime("%H:%M:%S",Time)
    print(Time)
    exist = os.path.exists(FileName)
    if exist == True:
        myFile = open(FileName,"a")
    else:
        myFile = open(FileName,"w")


    myFile.write(Time)
    myFile.write("\n")
    myFile.close()

def main():

   schedule.every(5).minutes.do(WriteTime)

   while True:
       schedule.run_pending()
       time.sleep(1)


if __name__ == "__main__":
    main()