import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    auth_plugin='mysql_native_password',
    autocommit = True
)

mycursor = mydb.cursor()

# Create the zoo database
mycursor.execute("DROP DATABASE IF EXISTS zoodatabase")
mycursor.execute("CREATE DATABASE zoodatabase")