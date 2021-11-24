"""
as per example 29,
if we want to store 10 months salary details,
then we need 10 objects
inside 10 bjects we can store 10 months salary details
"""

"""
If we need 10 objects then do we need to create 10 classes?
NOT Required
We can make ONE CLASS CAN PRODUCE 0 or MORE OBJECTS
"""

"""
Let us make one class to produce multiple objects
"""


class Month:

    employee_name = "abc"

    def __init__(self,s,r):
        self.salary = s
        self.rent = r


# Produce 2 copies of Month object and store values/data inside it
Month1 = Month(20000,10000)
# 1.objeact creation using __new__ method 2. initialise using __init__
# Month.__init__(Month1,20000,10000):
#   Month1.salary = 20000
#   Month1.rent = 10000

Month2 = Month(22000,10000)
# Month.__init__(Month2,20000,10000):
#   Month2.salary = 20000
#   Month2.rent = 10000

# Like this we can create n number of objects

print("Employee Name : ",Month.employee_name)

print("Month_1_salary : ",Month1.salary)
print("Month_1_Rent : ",Month1.rent)

print("Month_2_salary : ",Month2.salary)
print("Month_2_Rent : ",Month2.rent)

# Totally 3 objects
# 1). Month 2). Month1 3). Month2
# 1). Month : CLASS OBJECT
# 2). Month1 3). Month2 :- INSTANCE OBJECTS

# Totally 5 Variables
# 1). employee_name 2) salary 3) rent
# 1). employee_name : CLASS VARIABLES-> stored in class object
# 2) salary 3) rent :-> INSTANCE VARIABLES :- Storing in each Instance object create

