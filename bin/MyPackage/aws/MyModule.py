"""
This file is having one variable called 'dc_location'
AND
one function called 'log_process_function', if we pass server log
file path to this function, it will return list of ip,dt,im,url.

Since we need to reuse variable and function definitions in other programs/files/team/client/persom.
we are keeping in seperate .py file.

Since we are keeping only definitions,-
We call this file as PYTHON MODULE -OR General term is LIBRARY

"""

dc_location = "India"


def log_process_function(file_path):
    # Below code is copied from example 12th, and modified
    F1 = open(file_path, "r")
    final_result=[] # return =[(ip,dt,im,url),(ip,dt,im,url),(ip,dt,im,url),(ip,dt,im,url)]
    for my_line in F1:
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

            one_row_tuple = (ip,dt,im,url)
            final_result.append(one_row_tuple) # =[(ip,dt,im,url),(ip,dt,im,url),(ip,dt,im,url),(ip,dt,im,url)]

    F1.close()
    return final_result
