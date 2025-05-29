# Q2. Design python application which creates two threads as evenfactor and oddfactor. 
# Both the thread accept on parameter as integer. 
# EvenFactor thread will display additon of even factors of given number and oddfactor will display addition of odd factors
# of given number. After execution of both the thread gets completed main thread should display message as "exit from main".

import threading

def evenfactor(number):
    sum = 0
    for i in number:
        if(i % 2 == 0):
            sum += i
    print("Sum of even number : ", sum)
     
def oddfactor(number):
     sum = 0
     for i in number:
        if(i % 2 != 0):
              sum += i
     print("Sum of odd number : ", sum)

def main():
    print("Enter the even odd number range : ")
    size = int(input())
    num = []

    print("Enter the even odd number range : ")
    for i in range(size):
        num.append(int(input()))
    
    even_thread = threading.Thread(target=evenfactor,args=(num,))
    odd_thread = threading.Thread(target=oddfactor,args=(num,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()


if __name__ == "__main__":
    main()
print("exit form main...")