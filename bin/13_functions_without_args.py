"""
While CODING,
some part of the code, if we want to write more than one time (same code again ang again)
Option : 1 - We can copy and paste as many times as we want
Option : 2 - We can keep it one block and reuse - FUNCTION BLOCK
"""

print("Without using function")
print("-"*40)
# ------------------------

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

a = 10
b = 20
c = a + b
print("c : ", c)

print("-"*40)
# ------------------------

print("Using Function")
print("-"*40)
# ------------------------

def my_func():
    a = 10
    b = 20
    c = a + b
    print("c : ", c)


my_func()
my_func()
my_func()
my_func()
my_func()

print("-"*40)
# ------------------------

print("SSH Function Skeliton")
print("-"*40)
# ------------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)
    # paramiko -> SSH/FTP
    # subprocess -> localhost -shell command

my_ssh()
my_ssh()
my_ssh()
my_ssh()

print("-"*40)
# ------------------------
