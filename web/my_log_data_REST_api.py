"""
We need to expose log data to public,
so best way to expose data through API,
We are using REST style architecture to create API.
"""

import flask
my_app = flask.Flask("MyApp")

# REST API End Point
# http://127.0.0.1:5656/logreport
@my_app.route("/logreport")
def my_log_REST_API():
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

    # Any API should return json/xml only
    # return db_result in json format
    return flask.jsonify(db_result)


# ------------
# Run the server
# ------------
my_app.run(host="127.0.0.1",port=5656)
# ------------
