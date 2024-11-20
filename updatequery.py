import pymysql as mq

mysql=mq.connect(
        host="localhost",
        user="phpmyadmin",
        password="Phpmy@dm1n",
        database="school"
    )

mycursor=mysql.cursor()

name=input("Enter Name:-")

class_name=input("Enter Class:-")

st_id=input("Enter Id:-")

sql = "UPDATE students SET st_name=%s,st_class=%s WHERE st_id=%s"

data=(name,class_name,st_id)

try:
    mycursor.execute(sql,data)
    mysql.commit()
    print("Data Updated")
except:
    print("Error:-")
