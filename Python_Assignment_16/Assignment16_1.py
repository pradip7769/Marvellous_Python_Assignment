# Q1. Write a python program to create a text file named student.txt and write the names of 5 students into it.

import sys 
import os 

def main():

    if len(sys.argv) == 2: 
        if (sys.argv[1] == "--h"):
            print("This program is create a student file and write a Student name in file")
        elif (sys.argv[1] == "--u"):
            print("python File_Name.py student.txt")
        else:
            Student_Name = ["Pradip","Vishwanath","Kunal","Suraj","Amit"]
            print(sys.argv[1])
            exist = os.path.exists(sys.argv[1])
            print(exist)
            if exist == True:
               myFile = open(sys.argv[1] ,"w")
               print("File open succesfully...")

               for name in Student_Name:
                     myFile.write(name)
                     myFile.write("\n")
                     
               print("Student Name Write in successfull...")
               myFile.close()

            else:
                print("File is not exist")
                myFile = open(sys.argv[1] ,"w")
                print(myFile)
                print("File open succesfully...")

                for name in Student_Name:
                    myFile.write(name)
                    myFile.write("\n")

                print("Student Name Write in successfull...")
                myFile.close()
            
    else:
        print("Incorrect Input parameter received.")
        print("Use '--h' for help or '--u' for how to use")
                   

if __name__ == "__main__":
    main()