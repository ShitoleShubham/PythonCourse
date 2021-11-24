"""
To read web data : 'urllib'
To call any api : use library : 'requests'
"""
print("Weather Api")
my_city = input("Enter City To Know Weather : ")
my_weather_api = f'https://demoqa.com/utilities/weather/city/{my_city}'

import requests
print(f"Getting weather info for your city : {my_city}")
my_weather_api_response = requests.get(my_weather_api)
# requests.get, requests.post, requests.put, requests.delete, requests.patch
my_weather_api_response = my_weather_api_response.json()
print("Details Are : ")
for k,v in my_weather_api_response.items():
    print(k," : ",v)
print("Completed")


