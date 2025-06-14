# Q4. Write a Script that schedules multiple tasks: one to print "Lunch Time!" at a 1PM, and another to print "Wrap up work" at 6 PM.


import schedule 
import time 

def Luch_Time():
    print("Lunch Time!") 

def Wrap_Up_Work():
    print("Wrap up work") 


def main():
   
    schedule.every().day.at("15:06").do(Luch_Time)        # Will run at 15:05
    schedule.every().day.at("15:07").do(Wrap_Up_Work)      # Will run at 18:00

    while True:
       schedule.run_pending()
       time.sleep(1)


if __name__ == "__main__":
    main()