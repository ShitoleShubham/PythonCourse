"""
This is my another project, in this project we are making use of functions/variables
defined in MyModule.py (No need of copy/paste, we can use import)
"""

print("1-Way to Import")
print("-"*40)
# ----------------------

import MyModule
# import will execute MyModuel.py
# and bring 'dc_location' & 'log_process_function' objects to current environment
print("dc_location : ",MyModule.dc_location)
server_log_result = MyModule.log_process_function("../log/my_server_log.txt")
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------

print("2-Way to Import")
print("-"*40)
# ----------------------

import MyModule as mm
print("dc_location : ",mm.dc_location)
server_log_result = mm.log_process_function("../log/my_server_log.txt")
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------

print("3-Way to Import")
print("-"*40)
# ----------------------
# 1) import whichever you want
# 2) Not requreid to prefix with module name

# 1) import whichever you want
from MyModule import dc_location,log_process_function

print("dc_location : ",dc_location) # 2) Not requreid to prefix with module name
server_log_result = log_process_function("../log/my_server_log.txt")# 2) Not requreid to prefix with module name
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------


print("4-Way to Import")
print("-"*40)
# ----------------------
from MyModule import dc_location as dl,log_process_function as lpf

print("dc_location : ",dl) #
server_log_result = lpf("../log/my_server_log.txt")
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------


print("5-Way to Import")
print("-"*40)
# ----------------------
from MyModule import *

print("dc_location : ",dc_location)
server_log_result = log_process_function("../log/my_server_log.txt")
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------
print("If MyMoDULE.py is not in current directory then 2 options")
print("1. add PYTHOPATH env variable as shown in 'python_path_env.png' ")
print("2. Programatically we can add. as shown below")

print(r"Adding C:\Python_Training\lib folder to sys.PATH : ")
print("-"*40)
# ----------------------
import sys
sys.path.append(r"C:\python_training\lib")
print("SUCCESS")

print("import will look for the modules in below directories..")
print(sys.path)
print("-"*40)
# ----------------------

# If we have more than modules then we can keep/organise in folder/sub-folders
# Since these folders having 'modules', called as PACKAGES
# PACKAGES : Collection of modules & sub packages
# Module : Collection of variables/funcions definition/class defn.


print("1-Way to Import")
print("-"*40)
# ----------------------

import MyPackage.aws.MyModule
print("dc_location : ",MyPackage.aws.MyModule.dc_location)
server_log_result = MyPackage.aws.MyModule.log_process_function("../log/my_server_log.txt")
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------

print("2-Way to Import")
print("-"*40)
# ----------------------

import MyPackage.aws.MyModule as mm
print("dc_location : ",mm.dc_location)
server_log_result = mm.log_process_function("../log/my_server_log.txt")
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------

print("3-Way to Import")
print("-"*40)
# ----------------------
from MyPackage.aws.MyModule import dc_location,log_process_function

print("dc_location : ",dc_location) # 2) Not requreid to prefix with module name
server_log_result = log_process_function("../log/my_server_log.txt")# 2) Not requreid to prefix with module name
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------

print("4-Way to Import")
print("-"*40)
# ----------------------
from MyPackage.aws.MyModule import dc_location as dl,log_process_function as lpf

print("dc_location : ",dl) #
server_log_result = lpf("../log/my_server_log.txt")
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------

print("5-Way to Import")
print("-"*40)
# ----------------------
from MyPackage.aws.MyModule import *

print("dc_location : ",dc_location)
server_log_result = log_process_function("../log/my_server_log.txt")
print("server_log_result : ",server_log_result)

print("-"*40)
# ----------------------
