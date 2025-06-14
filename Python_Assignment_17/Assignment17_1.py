# Q1. Write a Python script that prints "Jay Ganesh...." every 2 seconds. Use the schedule.every(2).seconds.do(...) function.

import schedule
import time 


def Print():
    print("Jay Ganesh...")

def main():

    schedule.every(2).seconds.do(Print)

    while True:
        schedule.run_pending()
        time.sleep(2)
        


if __name__ == "__main__":
    main()