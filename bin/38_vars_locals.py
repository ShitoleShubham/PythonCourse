a = 10
b = 20
print("Varaibles list : ",locals())
print("-"*40)
# ----------------

def my_func():
    x = 20
    y = 30
    print("variables inside my_func : ",locals())
my_func()

print("-"*40)
# ----------------

class MyClass:
    def __init__(self):
        self.name = "abc"
        self.age = 20

m = MyClass()
print("Attributes inside m : ",vars(m))


print("-"*40)
# ----------------


