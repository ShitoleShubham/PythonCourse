"""
Using selenium library, test the

1. open the browser
2. Type the URL : https://www.google.com/
3. Find search box
4. type "Python"
5. Press Enter
6. Check "Python" is coming in title bar.
7. If it is coming then test case pass

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

my_options = Options()
my_options.headless = True

print("1. Opening the browser..",end="")
my_browser = webdriver.Chrome(options=my_options)
print("Done")

print("2. Type the URL..",end="")
my_browser.get("https://www.google.com/")
print("Done")

print("3. Find search box",end="")
my_search_field = my_browser.find_element_by_name("q")
print("Done")

print("4. type 'Python'..",end="")
my_search_field.send_keys("Python")
print("Done")

print("5. Press Enter")
my_search_field.send_keys(Keys.RETURN)
print("Done")

print('6. Check "Python" is coming in title bar...',end="")

assert "Python" in my_browser.title
# Why assert, instead of if else?
# assert will automatically throw error if condition fails
# assert will be used by many test framework
print("Done")
print("Test Case Success")

import time
time.sleep(5)
print("Closing Browser..",end="")
my_browser.close()
print("Done")