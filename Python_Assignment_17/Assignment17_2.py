# Q2. Schedule a task that displays the current date and time every minute using the datetime module.

import schedule 
import time 
import datetime

def printDateTime():
    now = datetime.datetime.now()
    print(now)

def main():

    schedule.every(1).minutes.do(printDateTime)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()