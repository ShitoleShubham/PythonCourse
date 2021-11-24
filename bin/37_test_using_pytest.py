"""
This program is to "test" developed programs/applications/etc
"""
"""
This program is STRICTLY FOR TESTING PURPOSE
"""
'''
we are using pytest framework to test out testcases
- pytest excpects each test case in seperate function
- function name should start with test_
- funcion should use 'assert' to check conditions
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def test_1_python_search():
    my_options = Options()
    my_options.headless = True

    print("1. Opening the browser..", end="")
    my_browser = webdriver.Chrome(options=my_options)
    print("Done")

    print("2. Type the URL..", end="")
    my_browser.get("https://www.google.com/")
    print("Done")

    print("3. Find search box", end="")
    my_search_field = my_browser.find_element_by_name("q")
    print("Done")

    print("4. type 'Python'..", end="")
    my_search_field.send_keys("Python")
    print("Done")

    print("5. Press Enter")
    my_search_field.send_keys(Keys.RETURN)
    print("Done")

    print('6. Check "Python" is coming in title bar...', end="")

    assert "Python" in my_browser.title
    # Why assert, instead of if else?
    # assert will automatically throw error if condition fails
    # assert will be used by many test framework
    print("Done")
    print("Test Case Success")

    print("Closing Browser..", end="")
    my_browser.close()
    print("Done")

def test_2_java_search():
    my_options = Options()
    my_options.headless = True

    print("1. Opening the browser..", end="")
    my_browser = webdriver.Chrome(options=my_options)
    print("Done")

    print("2. Type the URL..", end="")
    my_browser.get("https://www.google.com/")
    print("Done")

    print("3. Find search box", end="")
    my_search_field = my_browser.find_element_by_name("q")
    print("Done")

    print("4. type 'java'..", end="")
    my_search_field.send_keys("java")
    print("Done")

    print("5. Press Enter")
    my_search_field.send_keys(Keys.RETURN)
    print("Done")

    print('6. Check "java" is coming in title bar...', end="")

    assert "java" in my_browser.title
    # Why assert, instead of if else?
    # assert will automatically throw error if condition fails
    # assert will be used by many test framework
    print("Done")
    print("Test Case Success")

    print("Closing Browser..", end="")
    my_browser.close()
    print("Done")

def test_3_Perl_search():
    my_options = Options()
    my_options.headless = True

    print("1. Opening the browser..", end="")
    my_browser = webdriver.Chrome(options=my_options)
    print("Done")

    print("2. Type the URL..", end="")
    my_browser.get("https://www.google.com/")
    print("Done")

    print("3. Find search box", end="")
    my_search_field = my_browser.find_element_by_name("q")
    print("Done")

    print("4. type 'Perl'..", end="")
    my_search_field.send_keys("Perl")
    print("Done")

    print("5. Press Enter")
    my_search_field.send_keys(Keys.RETURN)
    print("Done")

    print('6. Check "Perl" is coming in title bar...', end="")

    assert "Perl" in my_browser.title
    # Why assert, instead of if else?
    # assert will automatically throw error if condition fails
    # assert will be used by many test framework
    print("Done")
    print("Test Case Success")

    print("Closing Browser..", end="")
    my_browser.close()
    print("Done")

def test_4_C_search():
    my_options = Options()
    my_options.headless = True

    print("1. Opening the browser..", end="")
    my_browser = webdriver.Chrome(options=my_options)
    print("Done")

    print("2. Type the URL..", end="")
    my_browser.get("https://www.google.com/")
    print("Done")

    print("3. Find search box", end="")
    my_search_field = my_browser.find_element_by_name("q")
    print("Done")

    print("4. type 'C'..", end="")
    my_search_field.send_keys("C")
    print("Done")

    print("5. Press Enter")
    my_search_field.send_keys(Keys.RETURN)
    print("Done")

    print('6. Check "C" is coming in title bar...', end="")

    assert "C" in my_browser.title
    # Why assert, instead of if else?
    # assert will automatically throw error if condition fails
    # assert will be used by many test framework
    print("Done")
    print("Test Case Success")

    print("Closing Browser..", end="")
    my_browser.close()
    print("Done")


# COMMANDS

# Command - 1:
# pytest 37_test_using_pytest.py

# Command - 2 (2 test cases in parallel):
# pytest -n 2 37_test_using_pytest.py

# Command - 3 (4 test cases in parallel):
# pytest -n 4 37_test_using_pytest.py
