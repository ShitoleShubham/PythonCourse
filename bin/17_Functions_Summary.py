"""
We can write function:
1. Functions with Positional Arguments
2. Functions with Positional Arguments and Default Values
3. Functions with VARIABLE Positional Arguments

AND

1. Functions with Keyword Arguments
2. Functions with Keyword Arguments and Default Values
3. Functions with VARIABLE Keyword Arguments

ARGUMENTS COMBINATIONS
"""

print("# 1 : without argument")
print("-"*40)
#---------------------

def add():
    a = 10
    b = 20
    c = a + b
    print("c : ",c)

add()

print("-"*40)
#---------------------

print("# 2 : with POSITIONAL args")
print("-"*40)
#---------------------

def add(a,b):
    return a+b

print(add(10,20))

print("-"*40)
#---------------------

print("# 3 : with POSITIONAL Args & default values")
print("-"*40)
#---------------------

def add(a,b=10):
    return a+b
print(add(10)) # CORRECT
print(add(10,20))# CORRECT

print("-"*40)
#---------------------


# 4 : ORDER OF THE ARGUMENT IS MANDATORY
# 1st Non-default, default, variable args, keyword args if any
#def add(a=10,b): # WRONG
#    return a+b


print("# 5: ORDER IS FINE")
print("-"*40)
#---------------------

def add(b,a=10): # CORRECT
    return a+b

print(add(10,20))

print("-"*40)
#---------------------

print("# 6: nondefaul+default+variable args")
print("-"*40)
#---------------------

def add(a,b=10,*c): # CORRECT
    return a+b+sum(c)
# NO OPTION TO SKIP b, 2nd arg will alwasy goto b
print(add(10,20,30,40,50,60))

print("-"*40)
#---------------------

print("# 7: nondefaul+default+variable args+keyword args")
print("-"*40)
#---------------------

def add(a,b=10,*c,d,e):
    return a+b+sum(c)+d+e
print(add(10,20,30,40,50,60,70,e=80,d=90))
#a=10, b=20,c=(30,40,50,60,70),e=80,d=90

print("-"*40)
#---------------------

print("# 8: nondefaul+default+variable args+keyword args+variable keywrod args")
print("-"*40)
#---------------------

def add(a,b=10,*c,d,e,**f):
    return a+b+sum(c)+d+e+sum(f.values())

print(add(10,20,30,40,50,60,70,e=80,d=90,x=100,y=200,z=300))
#a=10, b=20,c=(30,40,50,60,70),e=80,d=90, f={'x':100,'y':200,'z':300}

print("-"*40)
#---------------------


print("# 9: 2 positional and 2 keyword")
print("-"*40)
#---------------------

def add(a,b,*,c,d):
    return a+b+c+d

print(add(10,20,c=30,d=40))

print("-"*40)
#---------------------

print("# 10: 0 or more poitional")
print("-"*40)
#---------------------

def add(*a):
    return sum(a)
print(add())
print(add(10))
print(add(10,20))

print("-"*40)
#---------------------

print("# 11: 0 or more keyword only args")
print("-"*40)
#---------------------

def add(**a):
    return sum(a.values())

print(add())
print(add(x=10))
print(add(x=10,y=20))
print(add(x=10,y=20,z=30))

print("-"*40)
#---------------------

print("# 12: 0 or more poitional AND 0 or more keyword only args")
print("-"*40)
#---------------------

def add(*a,**b):
    return sum(a)+sum(b.values())

print(add())
print(add(10,20))
print(add(x=10,y=20))
print(add(10,20,x=10,y=20))

print("-"*40)
#---------------------

