#Q1 Create apython program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second. Use threading.Thread

import threading
import time

def Thread1():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def Thread2():
    for i in range(1,6):
        print(i)
        time.sleep(1)

def Thread3():
    for i in range(1,6):
        print(i)
        time.sleep(1)


def main():
    T1 = threading.Thread(target=Thread1)
    T2 = threading.Thread(target=Thread2)
    T3 = threading.Thread(target=Thread3)

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()
   

if __name__ == "__main__":
    main()
