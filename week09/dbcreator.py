import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3308"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE datarepresentation")