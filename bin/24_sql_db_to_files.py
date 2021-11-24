"""
Get data from SQL database "my_database.sqlite3"
and
produce csv,xlsx,json reports
"""
print("Dump data from DB to files")
import sqlite3
print("Creating/Connecting to 'my_database.sqlite3'...",end="") # default value of end="\n"
my_db_connection = sqlite3.connect("my_database.sqlite3")
print("SUCCESS")

print("Getting cursor object to run query..",end="")
my_cursor = my_db_connection.cursor()
print("SUCCESS")

my_query = "SELECT * FROM MY_LOG_DATA"
print(f"Executing : {my_query}")
my_cursor.execute(my_query)
print("SUCCESS")

print("Retreiving data from cursor object..",end="")
db_result = my_cursor.fetchall()
print("Success")

print("db_result : ",db_result,sep="\n")

import sys
size_of_db_result = sys.getsizeof(db_result)
print("size of db_result data is : ",size_of_db_result," bytes")
print("-"*40)
# ------------------------

print("1-Way : Dump data to csv/txt file")
print("-"*40)
# ------------------------

# as per examples in 11_file_operations.py

print("Connecting/Creating to db_dump_1.txt and db_dump_1.csv...",end="")
F1 = open("db_dump_1.txt","w")
F2 = open("db_dump_2.csv","w")
print("SUCCESS")

print("Write header..",end="")
print("IP","DATE","PICS","URL",sep="\t\t",file=F1,flush=True)
print("IP","DATE","PICS","URL",sep=",",file=F2,flush=True)
print("SUCCESS")

print("Writing db data to files...",end="")
for each_row_tuple in db_result:
    # Unpacking example : 15 & 16
    print(*each_row_tuple,sep="\t\t",file=F1,flush=True)
    print(*each_row_tuple,sep=",",file=F2,flush=True)
print("SUCCESS")


print("Closing file handles...",end="")
F1.close()
F2.close()
print("SUCCESS")

print("db reports generated successfully..")
print("Please check the reports 'db_dump_1.txt' and 'db_dump_2.txt'")

"""
>>> each_row_tuple=('123.123.123.123', '26/Apr/2000', 'wpaper.gif', 'http://www.jafsoft.com/asctortf/')
>>> print(each_row_tuple)
('123.123.123.123', '26/Apr/2000', 'wpaper.gif', 'http://www.jafsoft.com/asctortf/')
>>> print(*each_row_tuple)
123.123.123.123 26/Apr/2000 wpaper.gif http://www.jafsoft.com/asctortf/
>>> print(*each_row_tuple,sep="\t\t")
123.123.123.123		26/Apr/2000		wpaper.gif		http://www.jafsoft.com/asctortf/
>>> print(each_row_tuple,sep="\t\t")
('123.123.123.123', '26/Apr/2000', 'wpaper.gif', 'http://www.jafsoft.com/asctortf/')
>>> 
"""
print("-"*40)
# ------------------------
