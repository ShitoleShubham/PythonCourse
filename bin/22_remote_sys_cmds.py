"""
Execute remote sysmte commdand
and also copy the file from remote systme(FTP)
"""

import paramiko

print("Obtaining SSH clinet ..",end="")
ssh = paramiko.SSHClient()
print("Done")

# Known host
print("Adding HOST KEY POLICY TO ACCEPT THE CONNECTION ..",end="")
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
print("Done")

print("Connecting to remote host 'test.rebex.net' : ",end="")
ssh.connect(hostname='test.rebex.net',port=22,username='demo',password='password')
print("Success")

print("Executing 'ls' command : ",end="")
stdin, stdout, stderr = ssh.exec_command('ls')
print("Done")

print("Reading and printing output of 'ls' command")
print("-"*20)
#-----------------
cmd_out = stdout.read()
print(cmd_out)
print("-"*20)
#-----------------

print("Converting bytes to string")
print("-"*20)
#-----------------

cmd_out = cmd_out.decode()
print(repr(cmd_out)) # repr will not replace \n with newline

print("-"*20)
#-----------------

print("Starting SFTP... : ",end="")
sftp = ssh.open_sftp()
print("Done")

print("Copyig(ftp) 'readme.txt' from remote host ..")
sftp.get('readme.txt',"remote_readme.txt")
print("Copied successfully. Please check remote_readme.txt ")

print("Closing SFTP and SSH conection")
# sftp.put(localpath=,remotepath="")
sftp.close()

ssh.close()
print("Completed")