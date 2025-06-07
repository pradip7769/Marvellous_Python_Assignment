# Create a base class Person with name and age. 
# Derive a class Teacher with subject and salary. 
# Use super() to call base class constructor and print both. 


class Person : 
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        print("Person Name : ", self.name)
        print("Persong Age : ", self.age)


class Teacher(Person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.sub = subject
        self.sal = salary
        print("Teacher Subject : ", self.sub)
        print("Teacher Salary : ", self.sal)

def main():
    T1 = Teacher("Pradip",25,"C Programming", 25000)


if __name__ == "__main__":
    main()
    
         