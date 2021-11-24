"""
Operator overoloading
"""

class Employee:
    def __init__(self,n):
        self.name = n
    def __add__(self, other):
        return self.name + other.name

e1 = Employee("abc")
e2 = Employee("xyz")
result = e1 + e2 # e1.__add__(e2) # __add__(e1,e2)
print("result : ",result)

"""
C:\Python39\python.exe C:/python_training/bin/34_operator_overloading.py
Traceback (most recent call last):
  File "C:\python_training\bin\34_operator_overloading.py", line 12, in <module>
    result = e1 + e2
TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'

Process finished with exit code 1
"""
