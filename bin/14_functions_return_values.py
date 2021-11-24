"""
Use Functions : If we want to execute the same code more than one time

What if we want to access values present inside the functions??
-- No Direct access to the variables defined inside the class
-- Alternate Approach: We can send outside using 'return'
-- All variables values will get cleaned up (garbage collected), once function execution is completed.
"""

print("No Direct Access to variables")
print("-"*40)
# ---------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)


my_ssh()
# print("After executing function blcok, we can't directlty access like this : ",host) # BO DIRECT ACCESS
# above line will throw error

print("-"*40)
# ---------------------

print("Function with return 1 value")
print("-"*40)
# ---------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)
    return host

my_ssh() # Function execution completed BUT return value is not captured
captured_value = my_ssh() # Function execution completed and return value is captured in 'captured_value'
print("captured_value : ",captured_value)

print("-"*40)
# ---------------------


print("Function with return more than one value")
print("-"*40)
# ---------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)
    return host,port # (host,port)
    print("After return, statements will neve execute") # CODE UNreachable


captured_value = my_ssh()
print("captured_value : ",captured_value)

print("-"*40)
# ---------------------


print("Function with return more than one value list")
print("-"*40)
# ---------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ",host)
    print("Executing command on port : ",port)
    return [host,port]


captured_value = my_ssh()
print("captured_value : ",captured_value)

print("-"*40)
# ---------------------

print("Function with return more than one value dict")
print("-" * 40)
# ---------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ", host)
    print("Executing command on port : ", port)
    return {"host" : host, "port":port}



captured_value = my_ssh()
print("captured_value : ", captured_value)

print("-" * 40)
# ---------------------

print("Function with ONE LINER EXPRESSION return")
print("-" * 40)
# ---------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ", host)
    print("Executing command on port : ", port)
    return "https://" + host + ":" + str(port) # Evaluate and return the result



captured_value = my_ssh()
print("captured_value : ", captured_value)

print("-" * 40)
# ---------------------


print("Function with only return: will return 'None' ")
print("-" * 40)
# ---------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ", host)
    print("Executing command on port : ", port)
    return



captured_value = my_ssh()
print("captured_value : ", captured_value)

print("-" * 40)
# ---------------------

print("Function NOT HAVING return: will return 'None' ")
print("-" * 40)
# ---------------------

def my_ssh():
    host = "192.168.1.10"
    port = 123
    print("Executing command on host : ", host)
    print("Executing command on port : ", port)



captured_value = my_ssh()
print("captured_value : ", captured_value)

print("-" * 40)
# ---------------------
