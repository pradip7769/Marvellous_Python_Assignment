# Design automation script which performs following task.

# Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.
# Create on e Directory named as Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted.
# Name of that log file should contains the date and time at which that file gets created.
# Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
# Accept Mail id from user and send the attachment of the log file. 
# Mail body should contains statistics about the operation of duplicate file removal.

# Mail body should contains below things : 
#       Starting time of scanning
#       Total number of files scanned
#       Total number of duplicate files found 

import sys 
import os
import hashlib
import time 
import schedule

import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

Border = "_"*78

def CalculateCheckSum(path, BlockSize = 1024):
    fobj = open(path,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)
    fobj.close()

    return hobj.hexdigest()

#----------------------------------------------------------------------#

def FindDuplicate(DirectoryName):
    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)
    
    flag = os.path.exists(DirectoryName)
    if(flag == False):
        print("There is no such directory")
        exit()
    
    flag = os.path.isdir(DirectoryName)
    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateCheckSum(fname)

            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]
    
    print(Duplicate)
    DeleteDuplicate(Duplicate)

def DeleteDuplicate(MyDict):
    Result = list(filter(lambda x : len(x) > 1,MyDict.values()))
    print(Result)

    newdir = "Marvellous"
    if not os.path.exists(newdir):
        os.mkdir(newdir)
    LogFileName = time.ctime() + ".txt"
    LogFileName = LogFileName.replace(":","_")
    LogFileName = LogFileName.replace(" ","_")

    count = 0
    delete_count = 0
    
    LogFileName = os.path.join(newdir,LogFileName)
    print(LogFileName)
    myFile = open(LogFileName,"w")
    myFile.write(Border + "\n")
    myFile.write("Deleted File Name is : \n")
    myFile.write(Border)
    myFile.write("\n")

    for Value in Result:
        for subvalue in Value:
            count += 1
            if(count > 1):
                print("Deleted file : ", subvalue)
                myFile.write(subvalue)
                myFile.write("\n")
                os.remove(subvalue)
                delete_count +=1 
        count = 0
    
    myFile.write("\n")
    myFile.write(Border)
    myFile.write("\n")
    myFile.write("Total number of duplicate files found : " + str(delete_count))
    myFile.write("\n\n")
    myFile.write(Border)
    
    myFile.close()

    print("Total delted file : ", delete_count)
    
    to_mail_id = sys.argv[3]
    send_email_with_attachment(LogFileName,to_mail_id)


def send_email_with_attachment(file_path,to_email):
    print(f"Sending to : {to_email}")
    from_email = "temprory7769@gmail.com"
    password = "rvmokwakzgffkbdw" 

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Information of Log file"

    with open(file_path,"rb") as attachment:
        part = MIMEBase('application','octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',f"attachment; filename={os.path.basename(file_path)}")
        msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login(from_email,password)
        server.sendmail(from_email,to_email,msg.as_string())

    print("File sending Sucessfull")
    

def main():
    print(Border)
    print("------------------------- Marvellous Automation ------------------------------")
    print(Border)
    

    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This application is used to perform directory cleaning")
            print("This application is maintain all duplicate deleted file")
            print("Accept mail id from user and attach the log file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the given Script as : ")
            print("python Assignment22_1.py Demo interval gmail.com")
        
        # else:
            # Result = FindDuplicate(sys.argv[1])
            # DeleteDuplicate(Result)
    if(len(sys.argv) == 4):

        DirName = sys.argv[1]
        interval = int(sys.argv[2])
        schedule.every(interval).minutes.do(FindDuplicate,DirName)

        while True:
            schedule.run_pending()
            time.sleep(1)
        
    else:
        print("Invalid number of command line arguments")
        print("use the given flag as : ")
        print("--h : used to display the help")
        print("--u : used to display the usage")

    print(Border)    
    print("-------------------- Thank you for using our script --------------------------")
    print("------------------------- Marvellous Infosystem  -----------------------------")
    print(Border)


if __name__ == "__main__":
    main()

