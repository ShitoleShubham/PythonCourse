"""
Below command will display content of the log file.
capture the output of the command(i.e file content) and
extract
IP
DATE
PICS
URL
and
1) produce sys_cmd_report.txt
2) send mail to client/manager with this report
3) also  attach 'dir' command ouput

"type c:\python_training\log\my_server_log.txt"

"""

import subprocess
my_cmd = r"type c:\python_training\log\my_server_log.txt"

print("Executing Below command : ",my_cmd,sep="\n")
print("-"*40)
# ------------------------------------

my_cmd_output = subprocess.check_output(my_cmd,shell=True)
print(my_cmd_output)

print("-"*40)
# ------------------------------------

print("Type of my_cmd_output : ")
print("-"*40)
# ------------------------------------

print(type(my_cmd_output))

print("-"*40)
# ------------------------------------

print("Methods inside bytes class : ")
print("-"*40)
# ------------------------------------

print(dir(my_cmd_output))

print("-"*40)
# ------------------------------------

print("Converting from bytes to strings")
print("-"*40)
# ------------------------------------

my_cmd_output = my_cmd_output.decode()
print(type(my_cmd_output))

print("-"*40)
# ------------------------------------

print("Output in string")
print("-"*40)
# ------------------------------------

print(repr(my_cmd_output))

print("-"*40)
# ------------------------------------

# The below code is copied from example 9.

print("list_of_lines : ")
print("-"*40)
# ---------------------------
list_of_lines = my_cmd_output.split("\n")
print(list_of_lines)

print("-"*40)
# ---------------------------

print("Processing data : ")
print("-"*40)
# ---------------------------
F = open("sys_cmd_out.txt","w")
print("IP","DATE","PICS","URL",sep="\t\t",file=F,flush=True)
for my_line in list_of_lines:
    if my_line[:3].isdigit():

        # Below code is copied from example 7
        sp = my_line.split()

        ip = sp[0]

        dt = sp[3]
        dt = dt[1:dt.index(':')]

        im = sp[6]
        if im.startswith("/pics/"):
            im = im.lstrip("/pics/")
        else:
            im = "No Image"

        url = sp[10]
        url = url[1:-1]

        print("Writing output to file : ",ip, dt, im, url,sep="\t\t")
        print(ip,dt,im,url,sep="\t\t",file=F,flush=True)

print("-"*40)
# ---------------------------
print("Generated 'sys_cmd_out.txt'")

# ---------------------------
F.close()
print("Capture 'dir' command output as well..")

my_dir_output = subprocess.check_output('dir',shell=True)
my_dir_output = my_dir_output.decode()
print("Done")

print("Preparing Mail...")
print("-"*40)
# ----------------------

# ----------------------
# PART - 1 OF THE MAIL
# ----------------------

from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()

print("Adding To,From,Subjects... : ",end="")
# Add Info
msg["To"] = 'mahadevaprabhu.g@gmail.com,mahadevaprabhu.g@gmail.com'
msg["Subject"] = "Shell command report"
msg["From"] = "mahadevaprabhu.g@gmail.com"
print("Done")
# ----------------------
# PART - 2 OF THE MAIL
# ----------------------

print("Adding 'dir output ' as mail body..",end="")
# Add email body
# We are adding my_dir_output to body
from email.mime.text import MIMEText
mail_body = MIMEText(
    f"""
    Dear Sir/Madam,
    
    Please find the 'dir' command output below.
    {my_dir_output}
    
    Thank You !!
    
    """

)
msg.attach(mail_body)
print("Done")
# ----------------------
# PART - 3 OF THE MAIL
# ----------------------

# Add attachment
# If data in file the use below step
# F = open("sys_cmd_out.txt","r")
# my_cmd_output = F.read()
# F.close()

# In this case we have data in file as well as in variable 'my_cmd_output'
# Here i will use 'my_cmd_output' variable.
print("Attaching my_cmd_report.txt..",end="")
from email.mime.application import MIMEApplication

my_attachement = MIMEApplication(my_cmd_output)
my_attachement.add_header('Content-Disposition','attachment',filename="my_cmd_out.txt")
msg.attach(my_attachement)
print("Done")
# ----------------------
# PART - 4 OF THE MAIL
# ----------------------
# Send Mail

import smtplib

# mail server
print("Connecting to gmail stmp server..",end="")
my_server = smtplib.SMTP(host='smtp.gmail.com',port=587)
print("Done")

print("Starting TLS..",end="")
my_server.ehlo()
my_server.starttls()
my_server.ehlo()
print("Done")

# MAIL SERVER USER NAME AND PASSWORD
print("Logging in to SMTP serevr.. ",end="")
my_server.login(user='pythontraining25@gmail.com',password='Python123')
print("Done")
print("Sending Maile..",end="")
my_server.sendmail(msg["From"],msg["To"],msg.as_string())
print("Done")
print("Logout from SMTP server...",end="")
my_server.close()
print("Done")

print("-"*40)
# ---------------------------------------
