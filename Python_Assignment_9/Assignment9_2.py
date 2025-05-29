# Write a Python program using multiprocessing.
# Process to square a list of numbers using multiple processes.

import multiprocessing

def square(num):
    list = []

    for i in num:
        list.append(i*i)
    print(list)

def main():
    value = [1,2,3,4,5,6,7,8,9,10]
    P = multiprocessing.Process(target=square,args=(value,))

    P.start()
    P.join()

if __name__ == "__main__":
    main()

