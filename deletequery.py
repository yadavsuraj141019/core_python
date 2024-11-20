import pymysql as mq

mysql=mq.connect(
        host="localhost",
        user="phpmyadmin",
        password="Phpmy@dm1n",
        database="school"
    )

mycursor= mysql.cursor()

st_id = input("ENter Student Id:- ")

sql = "Delete From students where st_id=%s"

try:
    mycursor.execute(sql,st_id)
    mysql.commit()
    print("Student Delete")
except:
    print("Error:-")