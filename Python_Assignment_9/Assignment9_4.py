# Q4. Create a Python program that Compare execution time of summing number from 1 to 10 million
# using normal function, threading, and multiprocessing.

import time
import multiprocessing
import threading

def sum():
    add = 0
    for i in range(10000001):
        add += i

def main():

    start_time = time.time()
    sum()
    stop_time = time.time()

    print("normal_fun : ", stop_time - start_time)
    
    start_time = time.time()
    T1 = threading.Thread(target=sum)
    T1.start()
    T1.join()
    stop_time = time.time()

    print("Thread : ", stop_time - start_time)

    start_time = time.time()
    P = multiprocessing.Process(target=sum)
    P.start()
    P.join()
    stop_time = time.time()

    print("Process : ", stop_time - start_time)


if __name__ == "__main__":
    main()



        