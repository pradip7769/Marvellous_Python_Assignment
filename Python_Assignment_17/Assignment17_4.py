# Q4. Create a task that runs once every day at 9:00 AM and prints "Namskar..."


import schedule 
import time 


def Print():
    print("Namskar...")


def main():

    schedule.every().day.at("9:00").do(Print)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()