# Q8. Write a script that simulates checking for email updates every 10 seconds. 
# (Use a print statement like "Checking mail..." instead of real email logic)


import schedule 
import time 

def checkMail():
     
     Time = time.localtime()
     Time = time.strftime("%H:%M:%S",Time)
     print("[" + Time  + "] Checking mail...") 


def main():
     
     schedule.every(10).seconds.do(checkMail)

     while True:
       schedule.run_pending()
       time.sleep(1)


if __name__ == "__main__":
    main()