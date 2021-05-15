import os
import pymysql

#Get username from workspace
#Modify this varible if running on another environment
username = os.getenv('C9_USER')

#Connect to the Database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    #run a query
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-6 23:04.56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        

finally:
    #close the connection
    connection.close()
