"""
In this sectiomn,
we will discuss about
if, for loop, while
"""
"""
If statement In other language
s1
if condn{
    s2
        s3
s4
    s5
}
s6

In python instead of {}, we will use indentation
s1
if condn:
    s2
    s3
    s4
    s5
s6

"""
print("If example")
print("-"*40)
# --------------------------
x = 10
s = "Python"
L1 = [10,20,30]
L2 = [10,20,30]
D = {"A" : 10 , "B" : 20}

if (x == 10) and ("th" in s) and (L1 == L2) and (20 in L1) and ("A" in D.keys()):
    print("All conditions True")
elif x>10:
    print("X is gt 10")
else:
    print("All conditions failed")

print("-"*40)
# --------------------------

print("for loop example")
print("-"*40)
# --------------------------
# for loop - iterate any collection
# str, list, tuple, dict etc
# In for loop also we can use break, continue, else
a = "Python"

for i in a:
    print("each char : ",i)
    print("each char : ", i)
    print("each char : ", i)

print("-"*40)
# --------------------------

# Observarions
# 1) for loop will end after completing all elements in the collection
# 2) for loop will excute all statements for each element

# Observarions
# 1) for loop will end after completing all elements in the collection
# If we want to end for loop in between then use 'break' statement

L = [10,20,30]
for i in L:
    if i > 10:
        break
    print("i in L : ", i)
    print("i in L : ", i)

print("Outside for loop")
print("-"*40)
# --------------------------


# Observarions
# 1) for loop will end after completing all elements in the collection
# 2) for loop will excute all statements for each element
# We will use 'continue' to skip current iteration and proceed to next iteration

D = {"A" : 10, "B" : 20, "C" : 30}
for v in D.values():
    if v <= 10:
        continue # Goto next iteration
    print("Value in D is : ",v)

print("Outside the for loop")
print("-"*40)
# --------------------------

print("while loop")
print("-"*40)
# --------------------------

s = "Python"
i = 0
while i < len(s):
    print("i in while : ",s[i])
    i = i + 1

print("Outside the while")
# In while also we can use break, continue, else

print("-"*40)
# --------------------------

print("for with else")
print("-"*40)
# --------------------------
L = ["prd_s1","prd_s1","prd_s1","stg_s1"]
# Findout are there any prod server in the list
# Print found or not found
for i in L:
    if i.startswith("prd"):
        print("Found")
        break
else:
    print("Not Found")

# point : 1 -  After completing for loop, else will execute
# point : 2 -  if for loop ended using 'break', the else 'break' will comeout of even else block



print("-"*40)
# --------------------------

