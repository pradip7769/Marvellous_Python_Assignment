# Demonstrate private, protected and public access modifiers using a class Employee with attributes: __salary, _department, name 

class Employee:
    def __init__(self,name,department,salary):
        self.name = name                          # Public
        self._department = department             # Protected
        self.__salary = salary                    # Private

    def Display(self):
        print("Employee Name : ", self.name)
        print("Employee Department : ", self._department)
        print("Employee salary : ", self.__salary)

def main():
    e = Employee("Pradip", "Embedded", 25000)
    e.Display()

if __name__ == "__main__":
    main()