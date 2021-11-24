"""
point - 1 : Use Functions : If we want to execute the same code more than one time
point - 2 : use arguments to make same function can be re used for different parametrs
    Ex: in our example, if we can pass values to host & port then we can reuse same function
    for different hosts as well

In this section,
1. Functions with Positional Arguments
2. Functions with Positional Arguments and Default Values
3. Functions with VARIABLE Positional Arguments
"""
print("1. Functions with Positional Arguments")
print("-"*40)
# --------------------------

def my_ssh(host,port):
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)

my_ssh("192.168.1.10",123)
my_ssh("192.168.1.11",123)
my_ssh("192.168.1.12",123)
my_ssh("192.168.1.13",124)

print("-"*40)
# --------------------------

print("2. Functions with Positional Arguments and default values")
print("-"*40)
# --------------------------

def my_ssh(host,port=123):
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)

my_ssh("192.168.1.10")
my_ssh("192.168.1.11") # Defult value 123 will be used
my_ssh("192.168.1.12",123) # No Problem
my_ssh("192.168.1.13",124)

print("-"*40)
# --------------------------

print("3. Functions with VARIABLE Positional Arguments") # FUNCTION OVERLOADING
print("-"*40)
# --------------------------

#def my_ssh(emp_name, emp_comp):
#def my_ssh(emp_name, emp_comp,email):
#def my_ssh(emp_name, emp_comp,email,phone):
#def my_ssh(emp_name, emp_comp,email,phone, addr1):
#def my_ssh(emp_name, emp_comp,email,phone, addr1,addr2):

def my_ssh(host,port,*my_cmds):
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)
    print("my_cmds : ",my_cmds)
    for i in my_cmds:
        print(i)


my_ssh("192.168.1.10",123) # host="192.168.1.10" , port=123, my_cmds=()
my_ssh("192.168.1.11",123,"ls") # host="192.168.1.11" , port=123, my_cmds=('ls')
my_ssh("192.168.1.12",123,"ls","dir")  # host="192.168.1.12" , port=123, my_cmds=('ls','dir')
my_ssh("192.168.1.13",124,"ls","dir",'date')  # host="192.168.1.12" , port=123, my_cmds=('ls','dir','date')

print("-"*40)
# --------------------------

print("Packing and Unpacking")
print("-"*40)
# --------------------------
# Assume, we are getting data from file and we got below list
L = ["192.168.1.13",124,"ls","dir",'date']
# How to pass each element of the list to my_ssh function?

# Option : 1 : DIFFICULT IF LIST SIZE IS HUGE AND UNKNOWN
my_ssh(L[0],L[1],L[2],L[3],L[4])

# Option : 2 : UNPACKING
my_ssh(*L) # *L will take care of passing each element of the list as argument
# *L wil make function call = my_ssh("192.168.1.13",124,"ls","dir",'date')
print("-"*40)
# --------------------------
