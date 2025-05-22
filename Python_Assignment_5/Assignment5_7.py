#Q7. Area and Perimeter of Rectangle 
# Accept the length and width of rectangle. Calculate and display the area and perimeter. 
# Expected Input : Enter length: 5 Enter width: 3
# Expected Output : Area : 15, Perimeter : 16
def Area(l,w):
    return l * w

def Perimeter(l,w):
    return 2*(l + w)

def main():
    print("Enter the Rectangle Length : ")
    length = int(input())
    print("Enter the Rectangel Width : ")
    width = int(input())

    area = Area(length,width)
    peri = Perimeter(length,width)

    print("Area : ", area)
    print("Perimeter : ", peri)

if __name__ == "__main__":
    main()

