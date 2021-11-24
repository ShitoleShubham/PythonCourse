"""
Read data from below url
http://www.jafsoft.com/searchengines/log_sample.html
and
Extract
IP
DATE
PICS
URL
and
insert into SQL database
"""

"""
Webscraping : Extracting data from website
We have many libraries like : BeatifulSoup, etc....
In our exmple, we are using regular expression to extract data
"""

"""
SQL Database
Python Program      --Communicate-->    External Database
Python Program      --Communicate-->    SQL Database/No-SQL database
Python Program      --Communicate-->    No-Sql Database like mongodb etc..
Python Program      --Communicate-->    SQL Databases like Oracle, Mysql, sqlite etc

Python Program      --Communicate using library-->    No-Sql Database like mongodb etc..
Python Program      --Communicate using library-->    SQL Databases like Oracle, Mysql, sqlite etc

Python Program      --Communicate using library (PyMongo)-->    No-Sql Database like mongodb etc..
Python Program      --Communicate using library (cx_Oracle)-->    SQL Databases like Oracle, Mysql, sqlite etc

in our example, we are using SQL database -> Sqlite

Python Program      -- library (sqlite3)-->    Sqlite Database

We need 
1) library (sqlite3)
2) Sqlite Database

We have
1) library (sqlite3) : Preinstalled with python
2) Sqlite Database : Preinstalled with python
"""

"""
Our example steps:
Step-1 : Create database, database table and make it ready
Step-2 : Read website data
Step-3 : using regular expression extract ip,date,image,url
Step-4 : insert into table created in step-1
step-5 : save(commit) and disconnect(close) from db
"""

print("Step-1 : Create database, database table and make it ready")
print("-"*40)
# ------------------------------
import sqlite3
print("Creating/Connecting to 'my_database.sqlite3'...",end="") # default value of end="\n"
my_db_connection = sqlite3.connect("my_database.sqlite3")
print("SUCCESS")

# for ANY other sql databases
# example : mysql
# install pymysql library
# import pymysql
# my_db_connection = pymysql.connect(user="",password="",host="",port="",db="my_database")

my_query ="""
CREATE TABLE IF NOT EXISTS MY_LOG_DATA(
IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100)
)
"""
print("Getting cursor object to run query..",end="")
my_cursor = my_db_connection.cursor()
print("SUCCESS")

print(f"Executing : {my_query}")
my_cursor.execute(my_query)
print("SUCCESS")

print("Step-1 Completed")
print("-"*40)
# ------------------------------

print("Step-2 : Read website data")
print("-"*40)
# ------------------------------
import urllib.request as u
my_url = 'http://www.jafsoft.com/searchengines/log_sample.html'
print("Connecting to website url..",end="")
F = u.urlopen(my_url)
# F.read(), F.readline, F.readlines, for loop etc
print("Success")

print("Step-3 : using regular expression extract ip,date,image,url")
print("-"*40)
# ------------------------------
import re
# as per our requirement, we need to check each line and extract
for my_line in F:
    # print(my_line)
    # print("type : ",type(my_line))
    # Since regex function expects string, we are converting to str
    my_line = my_line.decode()
    # print("type : ", type(my_line))
    # m = re.match("WHICH PATTERN?","WHICH STRING?")

    # m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*',my_line)
    # see below comment for explination

    # m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[A-Z][a-z]{2}/\d{4}).*', my_line)
    # m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[A-Z][a-z]{2}/\d{4}).*GET\s+/(pics/(\w+\.(jpg|png|gif)))?.*', my_line)
    # m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[A-Z][a-z]{2}/\d{4}).*GET\s+/(pics/(\w+\.(jpg|png|gif)))?.*?(http://\S+)">.*',my_line)
    # m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[A-Z][a-z]{2}/\d{4}).*GET\s+/(pics/(\w+\.(jpg|png|gif)))?.*?(http://.*)">.*',my_line)
    m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[A-Z][a-z]{2}/\d{4}).*GET\s+/(pics/(\w+\.(jpg|png|gif)))?.*?(http://[a-zA-Z0-9/._]+)">.*',my_line)
    # \S+ will Match till ">
    if m is not None:
        print("Complete Matched Line : ",m)
        print("Extracting ip,date,pics,url")
        ip = m.group(1)
        print(ip)
        dt = m.group(2)
        print(dt)
        im = m.group(4)
        if im is None:
            im = "No Image"
        print(im)
        url = m.group(6)
        print(url)
        print("-"*40)
        # ----------------------
        # Step-4 : insert into table created in step-1
        print("Inserting data into table..")
        my_query = f"INSERT INTO MY_LOG_DATA VALUES('{ip}','{dt}','{im}','{url}')"
        print("Executing query : ",my_query)
        my_cursor.execute(my_query)
        print("SUCCESS")
        print("-"*40)
        # ----------------------

print("Saving Data")
my_db_connection.commit()
print("SUCCESS")

print("closing the db connection")
my_db_connection.close() # SAVE AND CLOSE : COMMIT IS NOT RQUIRED
print("SUCCESS")
print("Data extraction is completed and added to database as well")
print("Please check database : my_database.sqlite3")


'''
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "<A HREF="http://www.jafsoft.com/asctortf/">http://www.jafsoft.com/asctortf/</A>" "Mozilla/4.05 (Macintosh; I; PPC)"
We need to tell pattern for 'How complete line look like?'
OUR Complete line looks like 

'starting from IP address, 
then some chars, 
then 'DATE',
then some chars,
then pics
then some chars,
then url
then some chars
'

'''

'''
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "<A HREF="http://www.jafsoft.com/asctortf/">http://www.jafsoft.com/asctortf/</A>" "Mozilla/4.05 (Macintosh; I; PPC)"
We need to tell character by character
\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d
\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}
'''
"""
IDENTIFIERS
----------------
\d -> any ONE digit b/n 0-9
\D -> any ONE non-digit - except digit any one character
. -> any ONE any character
\. -> Strictly one DOT
[.] -> Strictly one DOT
[0-9] -> \d -> any ONE digit b/n 0-9
[0-5] -> any ONE digit b/n 0-5
\s -> One space
\S -> One non-space
\w -> word character -> [a-zA-Z0-9_]
\W -> non word character -> [^a-zA-Z0-9_]
\D == [^0-9]


Quantifiers
------------------
\d{3} -> internally it will produce \d\d\d
.{3} -> ...
\d{1,3} ->internally it will produce (\d|\d\d|\d\d\d)
[0-9]{3} -> internally it will produce [0-9][0-9][0-9]
\s{3}
Modifiers
-------------
* -> 0 or more times
+ -> 1 or more times
? -> 0 or 1 time
*? -> Non-Greedy (Try to give maximum)
+? -> Non-Greedy (Try to give maximum)
?? -> Non-Greedy (Try to give maximum)
"""

"""
Date:
(\d{1,2}/[A-Z][a-z]{2}/\d{4})
OR
(\d{1,2}/(Jan|Feb|)/\d{4})
"""

"""
>>> import re
>>> s="nfsnlkfjslksjflkfjsf.jldsfjslfj.34247832975clvlkdslkfj"
>>> 
>>> re.match("\d+",s)
>>> re.match(".*",s)
<re.Match object; span=(0, 54), match='nfsnlkfjslksjflkfjsf.jldsfjslfj.34247832975clvlkd>
>>> re.match("nfs.*",s)
<re.Match object; span=(0, 54), match='nfsnlkfjslksjflkfjsf.jldsfjslfj.34247832975clvlkd>
>>> re.match(".*jlds.*",s)
<re.Match object; span=(0, 54), match='nfsnlkfjslksjflkfjsf.jldsfjslfj.34247832975clvlkd>
>>> re.match(".*34247.*",s)
<re.Match object; span=(0, 54), match='nfsnlkfjslksjflkfjsf.jldsfjslfj.34247832975clvlkd>
>>> re.match(".*34247.*kd",s)
<re.Match object; span=(0, 49), match='nfsnlkfjslksjflkfjsf.jldsfjslfj.34247832975clvlkd>
>>> m=re.match(".*34247(.*)kd",s)
>>> m.group(1)
'832975clvl'
>>> 
"""