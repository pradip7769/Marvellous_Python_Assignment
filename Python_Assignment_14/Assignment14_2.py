# Q2 Write a class Rectangle with length and width. Add a method to compute area and perimeter. 
# Area : 50 , Perimeter : 30 

class Rectngle:
    def __init__(self,lenght,width):
        self.length = lenght
        self.width = width

    def Area(self):
        Area = self.length * self.width
        print("Area : ", Area)

    def Perimeter(self):
        P = 2 * (self.length + self.width)
        print("Perimeter : ", P)


def main():
    rect = Rectngle(5,10)
    rect.Area()
    rect.Perimeter()

if __name__ == "__main__":
    main()