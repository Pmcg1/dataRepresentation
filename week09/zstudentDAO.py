import mysql.connector
class StudentDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port="3308",
        database="datarepresentation"
        )

    def create(self,values):
        mycursor = self.db.cursor()
        sql="insert into student (name, age) values (%s, %s)"
        mycursor.execute(sql, values)
        self.db.commit()
        return mycursor.lastrowid

    def getAll(self):
        mycursor = self.db.cursor()
        sql="select * from student"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result

    def findByID(self, id):
        mycursor = self.db.cursor()
        sql="select * from student where id = %s"
        values=(id,)
        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        return result

    def update(self, values):
        mycursor = self.db.cursor()
        sql="update student set name= %s, age=%s where id=%s"
        mycursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        mycursor = self.db.cursor()
        sql="delete from student where id=%s"
        values=(id,)
        self.db.commit()
        print("delete done")

studentDAO = StudentDAO()