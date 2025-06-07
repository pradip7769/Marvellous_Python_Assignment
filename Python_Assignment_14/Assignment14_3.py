# Create a class Book with private attribute __price. Add methods to get and set the price. Show encapsulation. 

class Book :
    def __init__(self,price):
        self.__price = price

    def get(self):
        return self.__price
    
    def set(self,new_price):
        self.__price = new_price


def main():

    book = Book(500)
    ret = book.get()
    print("Book price is : ", ret)
    book.set(650)
    ret = book.get()
    print("New price is : ", ret)


if __name__ == "__main__":
    main()