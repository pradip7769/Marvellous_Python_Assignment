
#Q1. Design python application which creates two thread named as even and odd.
# Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers

import threading

def even(number):
    for i in number:
        if(i % 2 == 0):
             print("even:",i)
     
def odd(number):
     for i in number:
        if(i % 2 != 0):
             print("odd: ",i)

def main():
    print("Enter the 20 even odd number : ")
    data = []

    for i in range(20):
        data.append(int(input()))
    
    even_thread = threading.Thread(target=even,args=(data,))
    odd_thread = threading.Thread(target=odd,args=(data,))

    even_thread.start()
    even_thread.join()
    odd_thread.start()
    odd_thread.join()


if __name__ == "__main__":
    main()
