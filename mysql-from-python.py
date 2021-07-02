import os
import pymysql

# get username from
# (Modify this variable if running on another enivornment)

username = os.getenv("C9_USER")

# Connect to the database

connection = pymysql.connect(
    host="localhost", user=username, password="", db="Chinook")


try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, regardsless of whether the above was successful
    connection.close()