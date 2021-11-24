"""
Extract
IP
Date
Image
URL
from
below string, using methods present inside 'str' class

"""

in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

print("in_string : ",in_string,sep="\n")

sp = in_string.split()

ip = sp[0]

dt = sp[3]
dt = dt[1:dt.index(':')]

im = sp[6]
im = im.lstrip("/pics/")

url = sp[10]
url = url[1:-1]

print(ip,dt,im,url)


"""
>>> in_string = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

>>> 
>>> type(in_string)
<class 'str'>
>>> 
>>> type(in_string).__name__
'str'
>>> # Methods inside str class
>>> dir(in_string)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> # We know slicing as well
>>> # There are MANY WAYS TO Extract
>>> 
>>> in_string
'123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
>>> # Extract IP
>>> # 1-way
>>> index_of_first_space = in_string.index(' ')
>>> index_of_first_space
15
>>> ip=in_string[0:15]
>>> ip
'123.123.123.123'
>>> 
>>> # 2-way

>>> sp = in_string.split() # Default is SPACE
>>> sp
['123.123.123.123', '-', '-', '[26/Apr/2000:00:23:48', '-0400]', '"GET', '/pics/wpaper.gif', 'HTTP/1.0"', '200', '6248', '"http://www.jafsoft.com/asctortf/"', '"Mozilla/4.05', '(Macintosh;', 'I;', 'PPC)"']
>>> type(sp)
<class 'list'>
>>> ip = sp[0]
>>> ip
'123.123.123.123'
>>> 
>>> # Get Date
>>> dt = sp[3]
>>> dt
'[26/Apr/2000:00:23:48'
>>> index_of_first_colon = in_string.index(':')
>>> dt1 = dt[1:index_of_first_colon]
>>> dt1
'26/Apr/2000:00:23:48'
>>> index_of_first_colon = dt.index(':')
>>> dt1 = dt[1:index_of_first_colon]
>>> dt1
'26/Apr/2000'
>>> 
>>> # Image
>>> im = sp[6]
>>> im
'/pics/wpaper.gif'
>>> # Tkeout '/pics/'
>>> # 1-way : Tkeout '/pics/'
>>> im1 = im.lstrip("/pics/")
>>> im1
'wpaper.gif'
>>> 
>>> # 2-way : Tkeout '/pics/'
>>> im2 = im.replace("/pics/","")
>>> im2
'wpaper.gif'
>>> 
>>> # 3-way : Tkeout '/pics/'
>>> index_of_first_slash_frm_right = im.rindex("/")
>>> im3 = im[  index_of_first_slash_frm_right + 1    :    ] # No end index means till end
>>> im3
'wpaper.gif'
>>> 
>>> 
>>> # 4-way : Tkeout '/pics/'
>>> im4 = im.split("/")
>>> im4
['', 'pics', 'wpaper.gif']
>>> im4[2]
'wpaper.gif'
>>> im4[-1]
'wpaper.gif'
>>> 
>>> 
>>> # URL
>>> url = sp[10]
>>> url
'"http://www.jafsoft.com/asctortf/"'
>>> type(url)
<class 'str'>
>>> url = url[1:-1]
>>> # OR we can use similar to removal of "/pics/"
>>> url
'http://www.jafsoft.com/asctortf/'
>>> 
"""
