"""
Multiple inheritance
"""
"""
We need features from Newmonth class and also from ptax class which 
is already available
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

class NewMonth(Month):
    def set_tax(self,t):
        self.tax = t

    def get_tax(self):
        return self.tax

class ptax:
    def set_ptax(self,p):
        self.ptax = p
    def get_ptax(self):
        return self.ptax


class AnotherMonth(NewMonth,ptax):
    pass # Keeping block empty But it still inherits


Month1 = AnotherMonth()
Month1.set_salary(20000)
Month1.set_rent(10000)
Month1.set_tax(2000)
Month1.set_ptax(200)

Month2 = AnotherMonth()
Month2.set_salary(22000)
Month2.set_rent(10000)
Month2.set_tax(2200)
Month2.set_ptax(220)


print("Employee Name : ",Month.employee_name)

# print("Month_1_salary : ",Month1._salary) # This still works. But we made it private so not preffered to access like this
print("Month_1_salary : ",Month1.get_salary())
print("Month_1_Rent : ",Month1.get_rent())
print("Month_1_tax : ",Month1.get_tax())
print("Month_1_ptax : ",Month1.get_ptax())

print("Month_2_salary : ",Month2.get_salary())
print("Month_2_Rent : ",Month2.get_rent())
print("Month_2_tax : ",Month2.get_tax())
print("Month_2_ptax : ",Month2.get_ptax())