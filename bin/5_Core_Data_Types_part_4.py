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

print("6. set ")
print("-"*40)
# -------------------------

S1 = {10,10,10,"Python","Python","Python"} # Inside {}, if we give Key:Val then Dictionary
S2 = set({10,10,10,"Python","Python","Python"})

print(S1,S2,sep="\n")

# In any program, we will be using below 3 things
# 1. Variable
# 2. function
# 3. classes : Group of 1). Variables and 2). functions


print("Group of 1). Variables and 2). functions inside 'set' class :")
print(dir(S1)) # Shortcut - dir will list 1). Variables and 2). functions inside that class

print("-"*20)
# -------------------------
         
S2 = {10,20,30,40}
S3 = {30,40,50,60}

print("S2 & S3 are : ",S2,S3)
print("S2 union S3 are : ",S2.union(S3)) # {10,20,30,40,50,60}
print("S2 intersection S3 are : ",S2.intersection(S3)) # {30,40}
print("S2 difference S3 are : ",S2.difference(S3)) # {10,20}

"""
>>> S1 = {10,10,10,10,20}
>>> S1
{10, 20}
>>> dir(S1)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>>
"""

print("-"*40)
# -------------------------


print("6. frozenset ")
print("-"*40)
# -------------------------

S1 = frozenset({10,10,10,"Python","Python","Python"}) 
S2 = frozenset({10,10,10,"Python","Python","Python"})

print(S1,S2,sep="\n")

# In any program, we will be using below 3 things
# 1. Variable
# 2. function
# 3. classes : Group of 1). Variables and 2). functions


print("Group of 1). Variables and 2). functions inside 'set' class :")
print(dir(S1)) # Shortcut - dir will list 1). Variables and 2). functions inside that class

print("-"*20)
# -------------------------
         
S2 = frozenset({10,20,30,40})
S3 = frozenset({30,40,50,60})

print("S2 & S3 are : ",S2,S3)
print("S2 union S3 are : ",S2.union(S3)) # {10,20,30,40,50,60}
print("S2 intersection S3 are : ",S2.intersection(S3)) # {30,40}
print("S2 difference S3 are : ",S2.difference(S3)) # {10,20}

"""
>>> fs = frozenset({10,10,10,20})
>>> fs
frozenset({10, 20})
>>> dir(fs)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>>
"""

print("-"*40)
# -------------------------
