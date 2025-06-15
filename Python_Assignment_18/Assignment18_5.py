# Q5. Accept file name and one string from user and return the frequency of that string from file. 
# Input : Demo.txt  Marvellous 
# Search "Marvellous" in Demo.txt


import os 
import sys 

CompareKey = "Marvellous" 

def StringFreq():

    File = sys.argv[1]

    exist = os.path.exists(File)
    if exist:
        print("File exist in current Directory")

        myFile = open(File,"r")

        content = myFile.read()

        content = content.split()
        # print(content)
        
        Count = 0
        for word in content:
            if word == CompareKey:
                Count += 1

        myFile.close()

        return Count
    
    else:
        print("File is not exist in current directory")

def main():
    print("-" * 58)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "-h") or (sys.argv[1] == "-H")):
            print("This application is used to perform Directory cleaning")
            print("This is directory automation Script...")
        
        elif((sys.argv[1] == "-u") or (sys.argv[1] == "-U")):
            print("Use the given script as : ")
            print("ScriptName.py Demo.txt")
            print("Please provide valid absolute path")
        
        else:
           FreqCount = StringFreq()
           print("frequency of that string from file is : ", FreqCount)

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