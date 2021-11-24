"""
Encapsulation
"""

print("Without using class : Personal Loan Data")
print("-"*40)
# -----------------------------
# Example : Personal Loan Data

employee_name = "abc"

month_1_salary = 20000
month_1_rent = 10000

month_2_salary = 22000
month_2_rent = 10000


print("Employee Name : ",employee_name)

print("Month_1_salary : ",month_1_salary)
print("Month_1_Rent : ",month_1_rent)

print("Month_2_salary : ",month_2_salary)
print("Month_2_Rent : ",month_2_rent)


print("-"*40)
# -----------------------------

print("Using class : Personal Loan Data")
print("-"*40)
# -----------------------------


class Employee:
    name = "abc"


class Month1:
    salary = 20000
    rent = 10000


class Month2:
    salary = 22000
    rent = 10000

# Total 3 objects : Employee, Month1, Month2 -> CLASS OBJECTS
# Varoiables inside each class :-> Class variables -> Stored inside class object

# In this perticular case advtage of using class is,

# 1)
# Encapsulation : data is hidden inside each object.
# Only class objects are visible outside

# 2)
# It also helped us to group the elements

print("Employee Name : ",Employee.name)

print("Month_1_salary : ",Month1.salary)
print("Month_1_Rent : ",Month1.rent)

print("Month_2_salary : ",Month2.salary)
print("Month_2_Rent : ",Month2.rent)
