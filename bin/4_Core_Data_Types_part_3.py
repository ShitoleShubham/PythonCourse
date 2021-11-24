'''
Core Data Types
(OR Already avaiable option to store data)
(OR builtin option to store data)

1. Numbers

2. Strings

3. List : There is option to store more than one element
        - MUTABLE : After creating the list, throught the program we can modify
        - List will assign index to each values
        
4. Tuple : There is option to store more than one element
        - IMMUTABLE : After creating the tuple, throught the program we CAN'T modify
        - Tuple will assign index to each values

5. Dictionary : There is option to store more than one element
        - MUTABLE : After creating the dictionary, throught the program we can modify
        - Dict will help us to provide Key/Value pair --> json, No-SQL db 

6. Set : There is option to store more than one element
        - MUTABLE : After creating the set, throught the program we can modify
        - Keeps only unique values
        - We have methods related to sets & Unions -> union, intersection, difference etc
        - Ex : intersection -> give me common servers from both the list
        - Ex : intersection -> give me common person from both the games



7. frozenset : There is option to store more than one element
        - IMMUTABLE set

'''


print("5. Dictionary ")
print("-"*40)
# -------------------------

# course_details = ["Python" , 4 , "Online"]

course_details = {
    0                   : "Python" ,
    "Duration"          : 4 ,
    ("mode" , "india")  : "Online"
    }

course_details = dict({
    0                   : "Python" ,
    "Duration"          : 4 ,
    ("mode" , "india")  : "Online"
    })

# Keys can be any IMMUTABLE OBJECTS like Numbers, str, tuple, frozenset etc
# Values  : We can store any values

print("course_details : ",course_details)

print("Course Name : ",course_details[0])
print("Course Duration : ",course_details["Duration"])
print("Course Mode and location : ",course_details[("mode" , "india")])

# In any program, we will be using below 3 things
# 1. Variable
# 2. function
# 3. classes : Group of 1). Variables and 2). functions

print("Group of 1). Variables and 2). functions inside 'list' class :")
print(dir(course_details)) # Shortcut - dir will list 1). Variables and 2). functions inside that class

print("List of key in course_details : ",course_details.keys())
print("List of values in course_details : ",course_details.values())
print("List of items in course_details : ",course_details.items())

"""
>>> D={"A":10}
>>> dir(D)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> 
>>>
"""

print("-"*40)
# -------------------------

