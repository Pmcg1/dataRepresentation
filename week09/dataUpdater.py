import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3308",
    database="datarepresentation"
)

mycursor = mydb.cursor()

sql="update student set name= %s, age=%s where id=%s"
values=("Joe", 33, 1)

mycursor.execute(sql, values)

mydb.commit()
print("update done")