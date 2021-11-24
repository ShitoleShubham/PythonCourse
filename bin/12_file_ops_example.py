"""
Read 'my_server_log.txt' and extract
IP
Date
Image
URL

and produce 'my_server_log_report.txt' and 'my_server_log_report.csv'
"""

'''
Steps:
Step-1 : Connect to external file (open function)
Step-2 : Read/Write (Many ways)
Step-3 : Disconnect (1. flush : only save without disonnecting. 2. close : save & disconnect )
'''

# Step-1 : Connect to external file (open function)
# --------------------
print("Connecting/Creating 'my_server_log.txt' , 'my_server_log_report.txt' and 'my_server_log_report.csv' : ",end="")
F1 = open(r"C:\python_training\log\my_server_log.txt","r")
F2 = open("my_server_log_report.txt","w")
F3 = open("my_server_log_report.csv","w")
print("DONE")
# --------------------

# Step-2 : Read/Write (Many ways)
# --------------------
print("Writing heading line to both output files : ",end="")
# To write : 1.write, 2.writelines, 3.print

# for F2, let us use 1.write
F2.write("IP\t\tDATE\t\tPICS\t\tURL\n")
F2.flush()

# for F3, let us use 2.writelines
F3.writelines([ "IP," , "DATE," , "PICS," , "URL\n" ])
F3.flush()

print("Done")

# Below code is copied from example 9:

print("Processing data : ")
print("-"*40)
# ---------------------------

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

        print("Writing Row: ", ip, dt, im, url,sep="\t\t")
        # let us use 3.print
        print(ip,dt,im,url,sep="\t\t",file=F2,flush=True) # Default end="\n"
        print(ip, dt, im, url, sep=",", file=F3, flush=True)
        print("DONE")

print("All write completed")
print("-"*40)
# ---------------------------
print("Current F1 Seek pointer location is : ",F1.tell())

# Step-3 : Disconnect (1. flush : only save without disonnecting. 2. close : save & disconnect )
# ---------------------------
print("Closing all file connections.. : ",end="")
F1.close()
F2.close()
F3.close()
print("Completed")
print("Please check generated reports : - 'my_server_log_report.txt' and 'my_server_log_report.csv'")
