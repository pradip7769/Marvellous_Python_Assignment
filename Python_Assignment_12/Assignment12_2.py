# Q2 Write a program which contains one class named as Circle. 
# Circle class contains three instance variables as Radius, Area, Circumference.
# That class contains one class variable as PI which is initialise to 3.14
# Inside init mehtod initialise all instance variables to 0.0. 
# There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference(), Display()
# Accept method will accept value of Radius from user. 
# CalculateArea() method will calculate area of circle and store it into instance variable Area. 
# CalculateCircumference() method will calculate circumference of circle and store it into instance variable circumference.
# And Display() method will display value of all the instance variables as Radius, Area, Circumference.
# After designing the above class call all instance methods by creating multiple objects


class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0 
        self.Area = 0.0 
        self.Circumference = 0.0
    
    def Accept(self):
        print("Enter the value of radius : ", end= " ")
        self.Radius = int(input())
    
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius 

    def Display(self):
        print("Radius of Circle is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Circumference of Circle is : ",self.Circumference) 
        print("-" * 30)


def main():
    circle1 = Circle()
    circle1.Accept()
    circle1.CalculateArea()
    circle1.CalculateCircumference()
    circle1.Display()

    circle2 = Circle()
    circle2.Accept()
    circle2.CalculateArea()
    circle2.CalculateCircumference()
    circle2.Display()
     
    circle3 = Circle()
    circle3.Accept()
    circle3.CalculateArea()
    circle3.CalculateCircumference()
    circle3.Display()

if __name__ == "__main__":
    main()


        
