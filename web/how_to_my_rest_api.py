"""
Here we are calling our API.
Same as example 'how_to_call_api_ex_a.py'
"""

my_api_end_point = "http://127.0.0.1:5656/logreport"
import requests
my_api_reponse = requests.get(my_api_end_point)
my_api_reponse = my_api_reponse.json()
print("my_api_end_point is : ",my_api_end_point)
print("my_api_reponse : ",my_api_reponse)

F =open("my_api_reponse.csv","w")
for each_row in my_api_reponse:
    print(*each_row,sep=",",file=F,flush=True)
F.close()
print("Please check my_api_reponse.csv file")