# Design python application which creates three threads as small, capital, digits. 
# All the threads accepts string as parameter. Small thread display number of small charactes, 
# capital thread display number of capital characters and digit thread display number of digits.
# Display id nd name of each thread 

import threading

def small(character):
    print("Small Character : ")
    for i in character:
        if(i.islower()):
            print(i)

def capital(character):
    print("Upper Character : ")
    for i in character:
        if(i.isupper()):
            print(i)
   
def digits(character):
     print("digit : ")
     for i in character:
        if(i.isdigit()):
            print(i)

def main():
    print("Enter the character range : ")
    size = int(input())

    char = []
    print("Enter the character : ")
    for i in range(size):
        char.append(input())
    
    s = threading.Thread(target=small,args=(char,))
    c = threading.Thread(target=capital,args=(char,))
    d = threading.Thread(target=digits,args=(char,))

    s.start()
    s.join()
    c.start()
    c.join()
    d.start()
    d.join()

if __name__  == "__main__":
    main()