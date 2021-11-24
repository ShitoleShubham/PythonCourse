"""
Dump db data to files using pandas
inside pandas library, we have 2 main classes
1. Series -> Methods related to 1 dimentional data
2. DataFrame -> Methods related to 2 dimentional data
"""

"""
We can store 2 dimentional data in list/tuple
why we need to use DataFrame class?
Inside dataframe class we have many methods which is not in list/tuple
"""
# 2D lists
L1 = [[10,20,30],[40,50,60]]
L2 = list([[10,20,30],[40,50,60]])
print("2 dimentional lists are : ",L1,L2,sep="\n")
print("-"*40)
# -----------------------

import pandas as pd
df1 = pd.DataFrame([[10,20,30],[40,50,60]])
print("df1 : ",df1,sep="\n")

df2 = pd.DataFrame([[10,20,30],[40,50,60]],index=["r1","r2"],columns=["c1","c2","c3"])
print("df2 : ",df2,sep="\n")

print("-"*40)
# -----------------------

print("Methods inside list class")
print("-"*40)
# -----------------------

print(dir(L1))

print("-"*40)
# -----------------------

print("Methods inside dataframe class")
print("-"*40)
# -----------------------

print(dir(df1))

print("-"*40)
# -----------------------

print("Getting data from db")
print("-"*40)
# -----------------------

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

print("-"*40)
# -----------------------

print("Creating DataFrame from db_result")
print("-"*40)
# -----------------------

import sys
size_of_db_result = sys.getsizeof(db_result)
print("size of db_result data is : ",size_of_db_result," bytes")

db_result_df = pd.DataFrame(db_result,columns=["IP","DATE","PICS","URL"])
print("db_result_df")
print(db_result_df)

print("-"*40)
# -----------------------

print('''
        Creating DataFrame from cursor object to 
        avoid storing in db_result variable
        '''
      )
print("-"*40)
# -----------------------
print(f"Executing : {my_query}")
my_cursor.execute(my_query)
print("SUCCESS")

cur_result_df = pd.DataFrame(my_cursor,columns=["IP","DATE","PICS","URL"])

print("cur_result_df : ",cur_result_df,sep="")
print("Now we saved : ",sys.getsizeof(db_result)," Bytes")

print("-"*40)
# -----------------------

print("Generating csv,xlsx,json files..")
print("-"*40)
# -----------------------
cur_result_df.to_csv("db_dump_3.txt",sep="\t")
cur_result_df.to_csv("db_dump_4.csv")
cur_result_df.to_excel("db_dump_5.xlsx")
cur_result_df.to_json("db_dump_6.json")

print("Reports created successfully")
print("Please check db_dump_3.txt,db_dump_4.csv,db_dump_5.xslx,db_dump_6.json")
print("-"*40)
# -----------------------

print("Only IP Column")
print("-"*40)
# -----------------------

print(cur_result_df["IP"])

print("-"*40)
# -----------------------


print("Only IP Column count")
print("-"*40)
# -----------------------

print(cur_result_df["IP"].count())

print("-"*40)
# -----------------------

print("value_counts :PICS columns")
print("-"*40)
# -----------------------

pics_val_count = cur_result_df["PICS"].value_counts()
print(pics_val_count)

print("-"*40)
# -----------------------

print("Using DataFrame Plot to plot graph and matplotlib to show")
print("-"*40)
# -----------------------

import matplotlib.pyplot as plt
pics_val_count.plot()
plt.show()

print("-"*40)
# -----------------------

print("Reading txt file and generating csv,xlsx,json etc")
txt_df = pd.read_csv("db_dump_3.txt",sep="\t")
print(txt_df)
txt_df.to_json("dbdump_7.json")
txt_df.to_csv("dbdump_8.csv")
txt_df.to_excel("dbdump_9.xlsx")
print("Please check dbdump_7, dbdump_8 and dbdump_9 files")
print("-"*40)
# -----------------------

print("Plot and save bar graph")
print("-"*40)
# -----------------------
pics_val_count.plot.bar()
plt.title("Log Report")
plt.xlabel("Pics Name")
plt.ylabel("Value Counts")
plt.savefig("mygraph.png",bbox_inches="tight")
print("Graph saved : mygraph.png")
print("-"*40)
# -----------------------

print("Write pics value count to sheet-1 and graph to sheet-2 of excel")
print("-"*40)
# -----------------------

# We dont have method related to multiple sheets in DataFrame class
# But we have one more class inside pandas : ExcelWriter,
# We can use ExcelWriter to interact with multiple sheets

my_writer = pd.ExcelWriter("MyReport.xlsx",engine="xlsxwriter")
# Engine means -> Which writer you want to use?
print("Methods inside ExcelWriter class")
print("-"*20)
# -----------------------

print(dir(my_writer))

print("-"*40)
# -----------------------

print("Write values count to sheet1...",end="")
print("-"*40)
# -----------------------

pics_val_count.to_excel(my_writer,sheet_name="MyData")
print("Done")

print("-"*40)
# -----------------------

print("Getting reference to workbook object and adding new sheet")
print("-"*40)
# -----------------------
wb = my_writer.book
ws = wb.add_worksheet("MyGraph")

print("DOne")
print("-"*40)
# -----------------------

print("Adding image, save and exit")
print("-"*40)
# -----------------------

# ws.insert_image("Which Cell?","Which Image?")
ws.insert_image("B2","mygraph.png")
my_writer.close()
print("please check myreport.xlsx")

print("-"*40)
# -----------------------

print("Display data which is having .jpg extn")
print("-"*40)
# -----------------------


df3 = cur_result_df[cur_result_df["PICS"].str.endswith("jpg")]
print(df3)

print("-"*40)
# -----------------------

print("groupby")
print("-"*40)
# -----------------------

df4 = cur_result_df.groupby(["PICS"]).count()
print(df4)

print("-"*40)
# -----------------------

