"""
In example 30, at the time of creating the
objects we passed/stored data
BUT
Suppose if we dont have data at the time of object creation,
May create empty object and then later we may store/retreive
Then how to write?
"""
"""
We can add methods to set and get values throught the program
"""


class Month:
    employee_name = "abc"

    def set_salary(self,s):
        self._salary = s

    def get_salary(self):
        return self._salary

    def set_rent(self,r):
        self._rent = r

    def get_rent(self):
        return self._rent

Month1 = Month()
Month1.set_salary(20000)
Month1.set_rent(10000)

Month2 = Month()
Month2.set_salary(22000)
Month2.set_rent(10000)


print("Employee Name : ",Month.employee_name)

# print("Month_1_salary : ",Month1._salary) # This still works. But we made it private so not preffered to access like this
print("Month_1_salary : ",Month1.get_salary())
print("Month_1_Rent : ",Month1.get_rent())

print("Month_2_salary : ",Month2.get_salary())
print("Month_2_Rent : ",Month2.get_rent())

