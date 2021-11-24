"""
Python web frameworks

Bottle  -> MICRO Framework
Flask  -> MICRO Framework
Falcon -> MICRO Framework


DJango -> Highly scalable application (MVT->Model View Template)
Web2py -> Highly scalable application (MVC->Model View Controller)
pyramib -> Highly scalable application (MVT->Model View Controller)
Many More....
"""

"""
Any web application neeeds
1) Web server
2) browser
3) database
"""

"""
All python web framework will be having
1) Web server -
2) database - sqlite
"""

"""
Except Falcon framework,
we can use any framework to develop
1) Website
2) Webservices (RESTFul Webservices /REST API)
3) Micro Services
"""

"""
we can use any framework to develop
1) Website
2) Webservices (RESTFul Webservices /REST API)
3) Micro Services

In this section,
we are discussing about
1) Website
"""

"""
Libraries
1. Module
2. Packages
3. Framework -> Not only having definitions, 
    it also contains partial implementation of common tasks
"""

import flask
my_app = flask.Flask("MyApp")

print("Methods inside flask class")
print("-"*40)
# ----------------------

print(dir(my_app))

print("-"*40)
# ----------------------

@my_app.errorhandler(404)
def my_own_error_page(err):
    return "Page Under Construction"


# http://127.0.0.1:1234/
# @my_app.route("/")
# def my_index_page():
#     return "<b>Wel Come</b>"

# End Point - 1
# http://127.0.0.1:1234/
@my_app.route("/")
def my_index_page():
    return flask.render_template("index.html")

# End Point - 2
# http://127.0.0.1:1234/about
@my_app.route("/about")
def my_about_page():
    return flask.render_template("about.html")

# End Point - 3
# http://127.0.0.1:1234/report
@my_app.route("/report")
def my_report_login_page():
    return flask.render_template("login.html")

# End Point - 4
# http://127.0.0.1:1234/validatelogin
@my_app.route("/validatelogin",methods=["post"])
def my_validate_db_report():
    # Retrieve username and password entered in front end
    # All the entered data will be stored in a
    # dictionary - flask.request.form
    # Retrieve from this dictionary

    entered_uname = flask.request.form.get("uname")
    entered_passwd = flask.request.form.get("pw")

    # connect to DB and check whether uname and password valid
    # here, we are hardcoding to 'abc' and 'xyz'
    if not (entered_uname == "abc" and entered_passwd == "xyz"):
        return "Invalid Credentials <a href='/report'>Go Back</a>"
    else:
        # Below code is copied from example 24
        import sqlite3
        print("Creating/Connecting to 'my_database.sqlite3'...", end="")  # default value of end="\n"
        my_db_connection = sqlite3.connect("../bin/my_database.sqlite3")
        print("SUCCESS")

        print("Getting cursor object to run query..", end="")
        my_cursor = my_db_connection.cursor()
        print("SUCCESS")

        my_query = "SELECT * FROM MY_LOG_DATA"
        print(f"Executing : {my_query}")
        my_cursor.execute(my_query)
        print("SUCCESS")

        print("Retreiving data from cursor object..", end="")
        db_result = my_cursor.fetchall()
        print("Success")
        # db_result =
        # [("123.123.123.123","20/Apr/2000","wpaper.gif","https://www.google.com")
        #  ("123.123.123.123","20/Apr/2000","wpaper.gif","https://www.google.com")
        # ]

        # db_result is list of tuples
        # We need to send whole result to html file
        # in html file, we need to write python code
        # to display data present in python list i.e db_result
        # Inside html,if we want to write python code then
        # use

        # For any statments,use thi : {% any statement%}

        # For any block like if, for then use write end block also Ex:
        #{% for ...%}
        #{% end %}

        # If we want to display python variable value thenuse
        # {{python_var_name}}

        # Who is executing python code in a browser?
        # Template engine will take care of executing python code in a browser
        # flask uses "JINJA2" template engine

        # In our case,
        # We will display log data in html table
        # table color -> green
        # highlight row which is having "No Image" with 'yellow'
        # highlight cell which is having "No Image" with 'red'

        return flask.render_template("logreport.html",my_data=db_result)


# End Point - 5
# http://127.0.0.1:1234/weather
@my_app.route("/weather")
def my_weather_page():
    return flask.render_template("getcity.html")


# End Point - 6
# http://127.0.0.1:1234/checkweather
@my_app.route("/checkweather",methods=["post"])
def weather_api_response_page():
    city = flask.request.form.get("mycity")
    api = f"https://demoqa.com/utilities/weather/city/{city}"
    import requests
    api_response = requests.get(api)
    api_response = api_response.json()
    return flask.render_template("weatherreport.html", my_data=api_response)



# ------------
# Start the server
# ------------
# my_app.run() # port=5000
my_app.run(host="127.0.0.1",port=1234)
# ------------



"""
>>> D = {"A":10,"B":20}
>>> D
{'A': 10, 'B': 20}
>>> dir(D)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> D["A"]
10
>>> D.get("A")
10
>>> D.get("C")
>>> D["C"]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    D["C"]
KeyError: 'C'
>>> #D["C"] # THIS WAY WILL THROW ERROR IF KEY NOT FOUND
>>> # D.get("C") # This will return None if key not found
>>>
"""
