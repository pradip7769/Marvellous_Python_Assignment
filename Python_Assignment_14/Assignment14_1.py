
# create a class Employee with attributes name, emp_id, and salary. 
# Cretate a objects of this class and print their details using a method. 
# Expected Output : 
# Name : Rohit, ID : 101 , Salary: 50000

class Employee:
    def __init__(self,name,emp_id,salary):
        self.Name = name 
        self.Emp_id = emp_id
        self.Salary = salary
    
    def EmpDetails(self):
        print("Employee Name : ",self.Name)
        print("Emplyee ID : ", self.Emp_id)
        print("Employee Salary : ", self.Salary)
    

def main():
    e1 = Employee("Rohit",101,50000)
    e1.EmpDetails()

if __name__  == "__main__":
    main()