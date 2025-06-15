# Q4. Write a program which accept two file names from user and compare contents of both the files. 
# If both the files contains same contents then display success otherwise display failure. 
# Accept names of both the files from command line. 

# Input : Demo.txt Hello.txt
# Compare contents of Demo.txt and Hello.txt 


import os 
import sys 

def CompareContent():

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    exist = os.path.exists(File1)
    if exist:
        print("File exist in current Directory")

        myFile1 = open(File1,"r")
        myFile2 = open(File2,"r")

        content1 = myFile1.read()
        content2 = myFile2.read()

        print(content1)
        print(content2)

        if content1 == content2:
            print("Content Match Successfull...")
        else:
            print("Content match failure...")
        

        myFile1.close()
        myFile2.close()
    
    else:
        print("File is not exist in current directory")

def main():
    print("-" * 58)

    if(len(sys.argv) == 3):
        if((sys.argv[1] == "-h") or (sys.argv[1] == "-H")):
            print("This application is used to perform Directory cleaning")
            print("This is directory automation Script...")
        
        elif((sys.argv[1] == "-u") or (sys.argv[1] == "-U")):
            print("Use the given script as : ")
            print("ScriptName.py ABC.txt Demo.txt")
            print("Please provide valid absolute path")
        
        else:
            CompareContent()

    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flag as : ")
        print("--h : used to display the help")
        print("--u : Used to display the usage")

    print("-" * 58)
    print("--------------Thank you for using our script--------------")
    print("-" * 58)

if __name__ == "__main__":
    main()