"""
Exceptions handling
"""

print("Without exception handling")
print("-"*40)
# ---------------------

# a = 10
# b = 0
# result = a/b # ERROR : Program will terminate here only
# print("result : ",result)

print("-"*40)
# ---------------------

print("Using try-except")
print("-"*40)
# ---------------------

try:
    a = 10
    b = 0
    result = a/b # ERROR : Program will terminate here only
    print("result : ",result)
except:
    print("Some Error")

print("-"*40)
# ---------------------

print("try-except with classes")
print("-"*40)
# ---------------------
# In the example above, all kind of exceptions will goto except block
# Then how to decide which exception occured?????
# SOLUTION : We can mention class name in except block

# 1. 'Exception' class is super class for all the exceptions classes

try:
    a = 10
    b = 0
    result = a/b # ERROR : Program will terminate here only
    print("result : ",result)
except ZeroDivisionError:
    print("It is ZDE")
except NameError as ne:
    print("it is Name error and captured thrown object is 'ne' is : ",ne)
except (KeyError,IndexError):
    print("KE or IE")
except Exception as e:
    print("Some error e is :",type(e))

print("-"*40)
# ---------------------

print("try-except-finally")
print("-"*40)
# ---------------------
try:
    a = 10
    b = 0
    result = a/b # ERROR : Program will terminate here only
    print("result : ",result)
except ZeroDivisionError:
    print("It is ZDE")
finally:
    print("IN FINALLY BLOCK : if any error in try block then also finally executes")
    print("IN FINALLY BLOCK : if any error in except block then also finally executes")
    print("IN FINALLY BLOCK : if NO error in try/except block then also finally executes")

print("-"*40)
# ---------------------


print("try-except-else")
print("-"*40)
# ---------------------
try:
    a = 10
    b = 0
    result = a/b
    # The below except block will handle only error occured till here
except ZeroDivisionError: # if error in try then except will execute and else will get skipped
    print("It is ZDE")
else: # if NO error in try then else will execute and except will get skipped
    result2 = b / a

print("-"*40)
# ---------------------

print("try-except-raise")
print("-"*40)
# ---------------------
try:
    a = 10
    b = 0
    if b == 0:
        raise ZeroDivisionError # Manually raising exception
    print('stmt-1')
    print('stmt-2')
    print('stmt-100')
    result = a/b
except ZeroDivisionError:
    print("From raise")

print("-"*40)
# ---------------------

print("try-except-assert")
print("-"*40)
# ---------------------
try:
    a = 10
    b = 0
    assert b != 0, "B should not equal to zero but it is equal"

    print('stmt-1')
    print('stmt-2')
    print('stmt-100')
    result = a/b
except AssertionError:
    print("From Assert")

print("-"*40)
# ---------------------


print("Custom Exception Class - 1")
print("-"*40)
# ---------------------

# Mandatory step is our class should be sub class of Exception
class MyError(Exception):
    pass

try:
    a = 10
    b = 0
    if b == 0:
        raise MyError
    result = a/b
except MyError as me:
    print("MyError is : ",me)

print("-"*40)
# ---------------------

print("Custom Exception Class - 2")
print("-"*40)
# ---------------------

# Mandatory step is our class should be sub class of Exception
class MyError(Exception):
    def __init__(self,m):
        self.msg = m
    def __str__(self):
        return self.msg

try:
    a = 10
    b = 0
    if b == 0:
        raise MyError("Here b is 0 so we are raising exception")
    result = a/b
except MyError as me:
    print("MyError is : ",me) # print internally calls __str__ of 'me' class

print("-"*40)
# ---------------------
