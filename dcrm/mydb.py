import mysql.connector

# create connection
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE jeremycompany")

print("Database created")
