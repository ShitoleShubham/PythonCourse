"""
Execute 'dir' command and print output
"""
import subprocess

print("Execute 'dir' command and print output")
print("-"*40)
# ------------------------
my_cmd = 'dir'

my_cmd_out = subprocess.check_output(my_cmd,shell=True)

print(f"my command '{my_cmd}' output is : ")
print(my_cmd_out)

print("-"*40)
# ------------------------



