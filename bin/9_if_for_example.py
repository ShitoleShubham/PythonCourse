"""
From the below SINGLE string, obtain list of lines then extract
IP
Date
Image
URL
from each line
"""

in_string = """
The following is a fragment from the server logs for JafSoft Limited. All the relative URLs are for the base URL http://www.jafsoft.com/.

First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
"""

print("-"*40)
# ---------------------------
print(r"in_string : (print replaces \n & \t with newline & tab space) ")
print("-"*40)
# ---------------------------

print(in_string)

print("-"*40)
# ---------------------------

print(r"in_string : use 'repr' function to display in raw format (\n\t as it is) ")
print("-"*40)
# ---------------------------

print(repr(in_string))

print("-"*40)
# ---------------------------

print("list_of_lines : ")
print("-"*40)
# ---------------------------

# How to obtain list of lines from string.
# >>> s="10\nPython"
# >>> s.split("\n")
# ['10', 'Python']
# >>>
# ---------------------------

list_of_lines = in_string.split("\n")
print(list_of_lines)

print("-"*40)
# ---------------------------

print("Processing data : ")
print("-"*40)
# ---------------------------
# Iterate line by line
# Check whether line is starting with IP address
# if it is starting with IP address then extract.

# Since we are not use regex, now how to check whether line is starting with IP address
# #
# >>> my_line = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] '
# >>> my_line[:3]
# '123'
# >>> my_line[:3].isdigit()
# True
# >>>

for my_line in list_of_lines:
    if my_line[:3].isdigit():

        # Below code is copied from example 7
        sp = my_line.split()

        ip = sp[0]

        dt = sp[3]
        dt = dt[1:dt.index(':')]

        im = sp[6]
        if im.startswith("/pics/"):
            im = im.lstrip("/pics/")
        else:
            im = "No Image"

        url = sp[10]
        url = url[1:-1]

        print(ip, dt, im, url,sep="\t\t")

print("-"*40)
# ---------------------------
