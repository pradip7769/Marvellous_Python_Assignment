#  Create a class Vehicle with methods start().
#  Derive class Car and override the method start() with additional behavior. 
#  Show method overiding.  

class Vehicle:
    def start(self):
        print("Vehicle is starting...")


class Car(Vehicle):
    def start(self):
        print("Car is starting...")
        super().start()

def main():
    c = Car()

    c.start()


if __name__ == "__main__":
    main()

