# Q4. Design automation script which accept directory name and mail id from user and create log file in that directory 
# which contains information of running processes as its name, PID, Username. After creating log file send that log file
# to the specified mail. 

# Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com 

# Demo is name of Directory.
# marvellousinfosystem@gmail.com is the mail id.

import psutil 
import sys 
import os 
import time 

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def ProcInfoLog(DirName):
    if not os.path.exists(DirName):
        os.makedirs(DirName)
    
    Time = time.ctime()
    FileName =  Time + ".txt"
    FileName = FileName.replace(":", "_").replace(" ", "_")
    
    FilePath = os.path.join(DirName, FileName)
    
    with open(FilePath, "w") as myFile:
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            myFile.write(f"Process Name: {proc.info['name']}, PID: {proc.info['pid']}, Username: {proc.info['username']}\n")

    return FilePath  


def send_email_with_attachment(file_path, to_email):
    print(f"Sending to: {to_email}")
    from_email = "temprory7769@gmail.com"
    password = "qeuixtbsdxtsvrjf"  

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Process Info Log File"

    with open(file_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(file_path)}")
        msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())


def main():
    if len(sys.argv) != 3:
        print("Usage: ProcInfoLog.py <DirectoryName> <RecipientEmail>")
        return

    directory = sys.argv[1]
    recipient_email = sys.argv[2]

    log_file_path = ProcInfoLog(directory)
    send_email_with_attachment(log_file_path, recipient_email)


if __name__ == "__main__":
    main()
