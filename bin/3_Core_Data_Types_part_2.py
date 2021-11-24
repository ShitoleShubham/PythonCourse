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

print("3. List ")
print("-"*40)
# -------------------------

L1 = [10,"Python", ["a" , "b"]]
L2 = list([10,"Python", ["a" , "b"]])

# It is indexed and we can do sling, step etc extactly like str
# So REFER : ex-2 and str_example.xlsx

print(L1,L2,sep="\n")

print("element at index 1 : ",L1[1]) #'Python'
print("2nd index char of element at index 1 : ",L1[1][2]) # 't'

# In any program, we will be using below 3 things
# 1. Variable
# 2. function
# 3. classes : Group of 1). Variables and 2). functions

print("Group of 1). Variables and 2). functions inside 'list' class :")
print(dir(L1)) # Shortcut - dir will list 1). Variables and 2). functions inside that class


print("-"*40)
# -------------------------

print("3. Tuple ")
print("-"*40)
# -------------------------

L1 = (10,"Python", ["a" , "b"])
L2 = tuple((10,"Python", ["a" , "b"]))

# It is indexed and we can do sling, step etc extactly like str
# So REFER : ex-2 and str_example.xlsx

print(L1,L2,sep="\n")

print("element at index 1 : ",L1[1]) #'Python'
print("2nd index char of element at index 1 : ",L1[1][2]) # 't'

# In any program, we will be using below 3 things
# 1. Variable
# 2. function
# 3. classes : Group of 1). Variables and 2). functions

print("Group of 1). Variables and 2). functions inside 'list' class :")
print(dir(L1)) # Shortcut - dir will list 1). Variables and 2). functions inside that class

"""
>>> L = [10,20]
>>> dir(L)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> T = (10,20)
>>> dir(T)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> 
>>> L
[10, 20]
>>> L.append(30)
>>> L
[10, 20, 30]
>>> M = [40,50,60]
>>> L.extend(M)
>>> L
[10, 20, 30, 40, 50, 60]
>>> T.index(20)
1
>>>
"""

print("-"*40)
# -------------------------
