# Q3 Design python application which creates two thread as evenlist and oddlist. 
# Both the threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input list 
# and display the addition.


import threading

def evenlist(number):
    sum = 0
    for i in number:
        if(i % 2 == 0):
            sum += i
    print("Sum of even number : ", sum)
     
def oddlist(number):
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
    
    even_thread = threading.Thread(target=evenlist,args=(num,))
    odd_thread = threading.Thread(target=oddlist,args=(num,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()


if __name__ == "__main__":
    main()

