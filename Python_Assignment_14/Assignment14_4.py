# Create a class Student with name, roll_no, and a class variable school_name. 
# print student details and school name. Change the school name using class name. 

class Student : 
    school_name = "COET"
    def __init__(self,name,roll_no):
        self.name = name 
        self.roll_no = roll_no

    def display(self):
        print("Name : ", self.name)
        print("roll no : ", self.roll_no)
        print("School name : ", Student.school_name)


def main():
    std = Student("Pradip",1028)
    std.display()
    Student.school_name = "COEP"
    std.display()

if __name__ == "__main__":
    main()