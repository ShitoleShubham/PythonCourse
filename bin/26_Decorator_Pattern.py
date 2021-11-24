"""
Decorator design pattern
"""

print("Without Decorator")
print("-"*40)
# ---------------

def my_func_1(a,b):
    print("Result is : ")
    print(a+b)
    print("End of Result")

def my_func_2(a,b):
    print("Result is : ")
    print(a-b)
    print("End of Result")

def my_func_3(a,b):
    print("Result is : ")
    print(a+b+a+b)
    print("End of Result")

my_func_1(10,20)
my_func_2(10,20)
my_func_3(10,20)

print("-"*40)
# ---------------

print("Using Decorator")
print("-"*40)
# ---------------

# How to reuse statements/logic etc which is common across all the functions?
# Solution : We can think of creating common function and put all common things there
# But
# How to design a function?

# The below function is not proper
# def my_common_func():
#     print("Result is : ")
#     print("End of Result")


# how to design the function?
# We can make use of solution given for this problem in one of the
# "DESIGN PATTERN" called "DECORATOR"

# TDecotor pattern will tell how you need to write function in this case
# The below function is written using steps given in the pattern


def my_decorator(my_function):
    def decorated_my_func(x,y):
        print("Result is :")
        my_function(x,y)
        print("End of Result")
    return decorated_my_func

@my_decorator
def my_func_1(a,b):
    print(a+b)

@my_decorator
def my_func_2(a,b):
    print(a-b)

@my_decorator
def my_func_3(a,b):
    print(a+b+a+b)

my_func_1(10,20)
my_func_2(10,20)
my_func_3(10,20)

print("-"*40)
# ---------------

print("Manually calling decorator to understand")
print("-"*40)
# ---------------

def my_decorator(my_function): # my_func_1
    def decorated_my_func(x,y):# decorated_my_func(10,20)
        print("Result is :")
        my_function(x,y) # my_func_1(10,20)
        print("End of Result")
    return decorated_my_func

def my_func_1(a,b):
    print(a+b)

returned_function = my_decorator(my_func_1)
# returned_function = decorated_my_func
returned_function(10,20) # decorated_my_func(10,20)


def my_func_2(a,b):
    print(a-b)

def my_func_3(a,b):
    print(a+b+a+b)


returned_function = my_decorator(my_func_1)
returned_function(10,20)

returned_function = my_decorator(my_func_2)
returned_function(10,20)

returned_function = my_decorator(my_func_3)
returned_function(10,20)


print("-"*40)
# ---------------
