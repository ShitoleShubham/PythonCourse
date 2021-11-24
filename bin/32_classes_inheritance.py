"""
Inheritance
Assume we already release 'Month' class long back,
Now we are getting new requirement to add new feature to
existing class 'Month'. Feature are 1) set_tax 2) get_tax methods
"""

'''
How to do?
Option - 1: (WRONG) can we copy existing class and modify?(NOT GOOD)
Ex: Assume existing class will have 10 and addign 2more to it - 12
now, even though we added 2 features, since we touched exisiting class
we need to test all 12 features
'''

"""
Option-1 : MORE COMPLEX, WE SHOULD NOT USE
OPTION-2 : Inheritance : Where we can extend exisitng class without
touching existing features. In extended class add new features and
test only new features. Taking remaining/existing methods from eisting
class will be taken care by our new class. WE NEED NOT TO BOTHER
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

# If we create object of NewMonth then we should be
# able to access all the properties of super class

Month1 = NewMonth()
Month1.set_salary(20000)
Month1.set_rent(10000)
Month1.set_tax(2000)

Month2 = NewMonth()
Month2.set_salary(22000)
Month2.set_rent(10000)
Month2.set_tax(2200)


print("Employee Name : ",Month.employee_name)

# print("Month_1_salary : ",Month1._salary) # This still works. But we made it private so not preffered to access like this
print("Month_1_salary : ",Month1.get_salary())
print("Month_1_Rent : ",Month1.get_rent())
print("Month_1_tax : ",Month1.get_tax())


print("Month_2_salary : ",Month2.get_salary())
print("Month_2_Rent : ",Month2.get_rent())
print("Month_2_tax : ",Month2.get_tax())


class MyList(list):
    def add_my_name(self,n):
        self.my_name = n
    def view_my_name(self):
        return self.my_name

L = MyList([10,20,30])
print("my list L : ",L)

L.append(10)
print("my list after append 10  : ",L)

L.add_my_name("XyZ")
print("MyName in MyList :  ",L.view_my_name())


class MyList2(list):
    def add_my_name(self,n):
        self.my_name = n
    def view_my_name(self):
        return self.my_name
    def append(self,m): # Polymorphism
        return f"Hello {m}"

L = MyList2([10,20,30])
print("my list L : ",L)


print("my list after append 10  : ",L.append(10))

L.add_my_name("XyZ")
print("MyName in MyList :  ",L.view_my_name())


"""
>>> s.encode(encoding="utf-8")
b'Hello'
>>> t=s.encode()
>>> t.decode()
"""

"""
>>> import getpass
>>> getpass.getpass("Enter Password :")
"""

