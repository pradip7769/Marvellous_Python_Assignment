# Accept file name and one string from user and return the frequency of that string from file. 

# Input : Demo.txt   Marvellous
# Search "Marvellous" in Demo.txt 

from collections import Counter
import sys 
import os 

def compareContents(file, string):

    count = 0
    check1 = os.path.exists(file)
    
    if check1 == True:
        with open(file) as f:
            content = f.read().split()
            print(content)
            # print(type(content))
            for i in content:
                # print(i)
                if i == "Marvellous":
                    count += 1 
            
        print("Number of the word in these files : ", count)        
    else:
        print("Fiel does not exists")
    



def main():

    if len(sys.argv) == 3: 
         file = sys.argv[1]
         string = sys.argv[2]
         compareContents(file,string)
    else:
         print("Wrong file name is received")

if __name__ == "__main__":
    main()