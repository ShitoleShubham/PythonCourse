"""
Till now we were storing values/data in a variable

Now,
we will interact with external file (text file with any extension like .txt,.csv, .log, .mylog, .yourlog)

Steps:
Step-1 : Connect to external file (open function)
Step-2 : Read/Write (Many ways)
Step-3 : Disconnect (1. flush : only save without disonnecting. 2. close : save & disconnect )
"""

# --------------------------
# Step-1 : Connect to external file (open function)
# --------------------------
print("Connecting/Creating external file 'out1.txt' .. : ",end="")# Default value for end is \n.
# F1 = open("filename/filepath","mode")
F1 = open("out1.txt","w")
print("Success")
# w mode will EMPTY the file if present ELSE create new file
# --------------------------

# --------------------------
# Step-2 : Write (Many ways) : 1. write 2.writelines 3. print function
# --------------------------

# 1. write
x = 10
s = 'Python\n'
print(repr(f"Writing {x} and {s} using 'write' method .. : ")) # f-> format-> replace {var_name} with value
x = str(x) + "\n" # write method expects 'str' objects
F1.write(x)
F1.write(s)
F1.flush()
print("Success")

# 2. writelines
x = 10
s = 'Python\n'
print(repr(f"Writing {x} and {s} using 'writelines' method .. : ")) # f-> format-> replace {var_name} with value
x = str(x) + "\n" # write method expects 'str' objects
F1.writelines([x,s]) # Any collection we can passlike str,list,tuple,dict,etc
F1.flush()
print("Success")

# 3. print
x = 10
s = 'Python\n'
print(repr(f"Writing {x} and {s} using 'print' method .. : ")) # f-> format-> replace {var_name} with value

# print will take of below 3 points
#----
# x = str(x) + "\n" # write method expects 'str' objects
# F1.writelines([x,s]) # Any collection we can passlike str,list,tuple,dict,etc
# F1.flush()
#----

print(x,s,sep="\n",file=F1,flush=True) # totally print will take 4 args : sep,end,file,flush

print("Success")
# --------------------------

# Step-3 : Disconnect (1. flush : only save without disonnecting. 2. close : save & disconnect )
# --------------------------
print("Closing 'out1.txt' connection .. : ",end="")
F1.close()
print("Success")

print("All Write Completed. Please check 'out1.txt'")
print("-"*40)
# --------------------------

############## READING ###############################
print("############## READING ###############################")

# --------------------------
# Step-1 : Connect to external file (open function)
# --------------------------
print("Connecting/Creating external file 'out1.txt' .. : ",end="")# Default value for end is \n.
# F1 = open("filename/filepath","mode")
F1 = open("out1.txt","r")
print("Success")
# r if file not present then it will not create. It is read only
# --------------------------

# --------------------------
# Step-2 : Read (Many ways) : 1. read 2.readline 3. readlines 4. for loop 5. list/tuple/set/dict/frozenset
# --------------------------

print("\nReading using '1. read' .. : ")
file_content = F1.read() # It reads complete file content and return 1 string
print("file_content : ",repr(file_content))

# Seek Pointer : -file operations will make use of this pointer

# 'a' mode : seek pointer will be pointing to end of the file
# 'w','r' mode : seek pointer will be pointing to beginning of the file (0th character)
# When we start writing /reading it will start from 0th character.
# In above 'read', it read complete file content from 0th char
# and seek reached end of the file. Again if we read without resetting seek, we will get empty

print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\nReading using '1. read' 2nd time .. : ")
file_content = F1.read() # It reads complete file content and return 1 string
print("file_content : ",repr(file_content))

# --------------------------
# 2. readline
print("-"*40)
# --------------------------

print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\nReading using '2. readline' .. : ")
file_content = F1.readline() # It reads one line
print("file_content : ",repr(file_content))

file_content = F1.readline() # It reads one line
print("file_content : ",repr(file_content))

file_content = F1.readline() # It reads one line
print("file_content : ",repr(file_content))

print("-"*40)
# --------------------------
print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\n Readline using while loop")
while True:
    my_line = F1.readline()
    if my_line == '': # EMPTY string is EOF
        break
    else:
        print(my_line)

print("-"*40)
# --------------------------


# --------------------------
# 3. readlines
print("-"*40)
# --------------------------

print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\nReading using '3. readlines' .. : ")
file_content = F1.readlines() # It reads complete file and return list of lines
print("file_content : ",file_content)

# --------------------------
# 4. for loop
print("-"*40)
# --------------------------

print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\nReading using '3. for loop' .. : ")

for my_line in F1: # For loop will take care of calling readline internally
    print("my_line in for : ",my_line)


# 6. list/tuple/dict/set etc
print("-"*40)
# --------------------------

print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\nReading using 'list' .. : ")
file_content = list(F1)
print("file_content list : ",file_content)

# --------------------------

print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\nReading using 'tuple' .. : ")
file_content = tuple(F1)
print("file_content list : ",file_content)

# --------------------------


print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\nReading using 'dict' .. : ")
file_content = dict(enumerate(F1)) # [(0,10),(1,python)]
print("file_content list : ",file_content)

# --------------------------


print("Resetting seek to 0th char.. : ",end="")
F1.seek(0)
print("Done")

print("\nReading using 'set' .. : ")
file_content = set(F1)
print("file_content list : ",file_content)

# --------------------------

# Step-3 : Disconnect (1. flush : only save without disonnecting. 2. close : save & disconnect )
# --------------------------
print("Closing 'out1.txt' connection .. : ",end="")
F1.close()
print("Success")

print("All Write Completed. Please check 'out1.txt'")
print("-"*40)
# --------------------------

import sys
print("SIZE OF file_content in BYTES : ",sys.getsizeof(file_content))

# --------------------------

# 'r' -> READ Only (If file not present then it will not create)
# 'w' -> Write only (Always EMPTY/New File)
# 'a' -> Append only (If file not exist then only it will create new file)
# 'r+' -> RW (If file not present then it will not create)
# 'w+' -> RW (Always EMPTY/New File)
# 'a+' -> RW (If file not exist then only it will create new file)

# --------------------------
