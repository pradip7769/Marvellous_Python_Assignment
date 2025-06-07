# Create a class Product with attributes name and price.
#  Implement __eq__ method to compare two products if they are equal in price. 

class Product:
    def __init__(self,name,price):
        self.name = name 
        self.price = price 

    def __eq__(self, other):
        return self.price == other.price


def main():

    p1 = Product("Laptop",50000)
    p2 = Product("Phone",50000)
    p3 = Product("Router",1200)

    if(p1 == p2):
        print("Product P1 & P2 Price are equal")
    else: 
        print("Product P1 & P2 Price are not equal")
    
    if(p1 == p3):
        print("Product P1 & P3 Price are equal")
    else:
        print("Product P1 & P3 Price are not equal")
   

if __name__ == "__main__":
    main()