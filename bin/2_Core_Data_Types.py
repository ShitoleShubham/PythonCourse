"""
This first MULTIPLE comment is used for documentation.
So, first comment of
1. Program
2. Function
3. class
are called "docstring"
"""

'''
This is also multiline comment only
Since this not a FIRST multiline comment, This is NOT documentation comment/string
'''
# This is one line comment

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

print("1. Numbers ")
print("-"*40)
# -------------------------

a = 10 
# No primitive data type in python - No declaring the variables
# for everything we have classes (either predefined / user defined)
# a = 10 then it will check 10 is of type int then it will call int class to
# create a object and store in a

# Manually we can also call class name
b = int(10)
print(a,b)

print("-"*40)
# -------------------------

print("2. Strings")
print("-"*40)
# -------------------------

a = 'PERSON'
b = "PERSON'S"
c = '''PERSON'''
d = """PERSON"""
e = 'PERSON\'S'
f = 'C:\newfolder\test.py' # Special Meaning Characters example : \n =-> replaced with newline and \t is replaced with TAB space
g = 'C:\\newfolder\\test.py' # No Special Meaning
h = r'C:\newfolder\test.py' # No Special Meaning : r-> raw string

print("a,b,c,d : ",a,b,c,d) # default sep="SPACE" # Between each element put SPACE
print("f : ",f,sep="\n") # Between each element put Newline
print("g : ",g,sep="\n") # Between each element put Newline
print("h : ",h,sep="\n") # Between each element put Newline

print("-"*20)
# -------------------------
i = "WEL COME"

# REFER str_example.xlsx

# Each char we have 2 indexes
#   1) +Ve index starting from 0, Left Side
#   2) -Ve index starting from -1, Right side 


print("char at 0 using +ve index : ",i[0])
print("char at 0 : using -ve index",i[-8])


print("char at 1 using +ve index : ",i[1])
print("char at 1 : using -ve index",i[-7])


print("Substring 1 to 6 using +ve index: ",i[1:6])
print("Substring 1 to 6 using -ve index: ",i[-7:-2])


print("Substring 1 to 6 using +ve index Step by 2 : ",i[1:6:2])
print("Substring 1 to 6 using -ve index Step by 2 : ",i[-7:-2:2])

print("Substring 1 to 6 using +ve index Step by 3 : ",i[1:6:3])
print("Substring 1 to 6 using -ve index Step by 3 : ",i[-7:-2:3])


print("-"*20)
# -------------------------

# Traverse Reverse
# Rightside of the string will become START OF THE STRING
# Leftside of the string will become END OF THE STRING

# print("Reverse : Substring 1 to 6 using +ve index: ",i[START INDEX OF THE STRING : END INDEX OF THE STRING])
print("Reverse : Substring 6 to 1 using +ve index 'i[1:6:-1]'EMPTY STRING : ",i[1:6:-1])

print("Reverse : Substring 6 to 1 using +ve index 'i[6:1:-1]' : ",i[6:1:-1])
print("Reverse : Substring 1 to 6 using -ve index 'i[-2:-7:-1])' ",i[-2:-7:-1])

print("Reverse : Substring 6 to 1 using +ve index 'i[6:1:-2]' : ",i[6:1:-2])
print("Reverse : Substring 1 to 6 using -ve index 'i[-2:-7:-2])' ",i[-2:-7:-2])

print("-"*20)
# -------------------------

# In any program, we will be using below 3 things
# 1. Variable
# 2. function
# 3. classes : Group of 1). Variables and 2). functions

a = 'PERSON' # Shortcut
b = str('PERSON') # Manually calling class name

print("Group of 1). Variables and 2). functions inside 'str' class :")
print(dir(a)) # Shortcut - dir will list 1). Variables and 2). functions inside that class





"""
>>> a = 'PERSON'
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> b=10
>>> dir(b)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> c = 12.5
>>> dir(c)
['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> 
>>>
"""


'''
>>> a = 'PERSON'
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> # Names WITHOUT having __, we NEED to call using THAT name
>>> # Ex:
>>> a
'PERSON'
>>> a.startswith("PER")
True
>>> 
>>> # Names having __, It is mapped to some OPERATORS OR some Functions. Internally those OPERATORS or FUNCTIONS will call.
>>> a
'PERSON'
>>> a = "WEL"
>>> b = "COME"
>>> a+b
'WELCOME'
>>> # a+b : Here + is calling __add__ internally
>>> a.__add__(b) # Manually also we can call
'WELCOME'
>>> a.__len__()
3
>>> len(a) # This len function internally calls : __len__
3
>>>
'''

print("-"*40)
# -------------------------
