"""
point - 1 : Use Functions : If we want to execute the same code more than one time
point - 2 : use arguments to make same function can be re used for different parametrs
AND
We were able to write functions in 2 ways
1. Functions with Positional Arguments
2. Functions with Positional Arguments and Default Values
3. Functions with VARIABLE Positional Arguments

NOW,
Since we have data stored in the form of Dictionary, json, no-sql databses where
key/value pair maintained
can we have all 3 types of functions mentioned above to take ARGUMENTS in the form of KY/VALUE pair

We GOT SOLUTION : We Can write function with KEYWORD ARGUMENTS
1. Functions with Keyword Arguments
2. Functions with Keyword Arguments and Default Values
3. Functions with VARIABLE Keyword Arguments

"""

print("1. Functions with Keyword Arguments")
print("-"*40)
# --------------------------

def my_ssh(*,host,port): # * tells, arguments coming after * will be keyword args
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)

my_ssh(host="192.168.1.10",port=123) # Since it is keyword args, mentioning arg name is mandatory
my_ssh(port=123,host="192.168.1.11")
my_ssh(host="192.168.1.12",port=123)
my_ssh(host="192.168.1.13",port=124)

print("-"*40)
# --------------------------

print("2. Functions with KEYWROD Arguments and default values")
print("-"*40)
# --------------------------

def my_ssh(*,host,port=123):
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)

my_ssh(host="192.168.1.10")
my_ssh(host="192.168.1.11") # Defult value 123 will be used
my_ssh(host="192.168.1.12",port=123) # No Problem
my_ssh(host="192.168.1.13",port=124)

print("-"*40)
# --------------------------

print("3. Functions with VARIABLE KEYWORD Arguments")
print("-"*40)
# --------------------------

def my_ssh(*,host,port,**my_cmds):
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)
    print("my_cmds : ",my_cmds)



my_ssh(host="192.168.1.10",port=123) # host="192.168.1.10" , port=123, my_cmds={}
my_ssh(host="192.168.1.11",port=123,mycmd1="ls") # host="192.168.1.11" , port=123, my_cmds={mycmd1:'ls'}
my_ssh(host="192.168.1.12",port=123,mycmd1="ls",mycmd2="dir")  # host="192.168.1.12" , port=123, my_cmds={'mycmd1':'ls','mycmd2':'dir'}
my_ssh(host="192.168.1.13",port=124,mycmd1="ls",mycmd2="dir",mycmd3='date')  # host="192.168.1.12" , port=123, my_cmds={'mycmd1':'ls','mycmd2':'dir','mycmd3':'date'}


print("-"*40)
# --------------------------

print("Packing and Unpacking")
print("-"*40)
# --------------------------
# Assume, we are getting data from file and we got below dict
D = {'host':"192.168.1.13",'port':124,'mycmd1':"ls",'mycmd2':"dir",'mycmd3':'date'}
# How to pass each element of the dict to my_ssh function?

# Option : 2 : UNPACKING
my_ssh(**D) # **D will take care of passing each element of the dict as argument
# **D wil make function call = my_ssh(host="192.168.1.13",port=124,mycmd1="ls",mycmd2="dir",mycmd3='date')
print("-"*40)
# --------------------------

print("Example:")
print("-" * 40)
# --------------------------

def my_ssh(*, host, port, **my_cmds):
    print("Executing command on host : ", host)
    print("Executing command on port : ", port)
    print("my_cmds : ", my_cmds)

    print("# 1-way to retrieve arguments from my_cmds")
    for my_arg, my_arg_value in my_cmds.items():
        print("Argument Name : ",my_arg)
        print("Argument Value is : ", my_arg_value)

    print("# 2-way to retriev")
    print(my_cmds['mycmd1'])
    print(my_cmds['mycmd2'])
    print(my_cmds['mycmd3'])



my_ssh( port=124, mycmd1="ls", mycmd2="dir",mycmd3='date',host="192.168.1.13")

print("-" * 40)
# --------------------------


"""
>>> D={"A":10,"B":20}
>>> for i in D:
	print(i)

	
A
B
>>> for i in D.keys():
	print(i)

	
A
B
>>> for i in D.values():
	print(i)

	
10
20
>>> for i in D.items():
	print(i)

	
('A', 10)
('B', 20)
>>> 
>>> for i,j in D.items():
	print("Arg name is : ",i)
	print("Arg name value is : ",j)

	
Arg name is :  A
Arg name value is :  10
Arg name is :  B
Arg name value is :  20
>>> 
"""