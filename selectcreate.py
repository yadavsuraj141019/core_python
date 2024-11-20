import pymysql as mq

mysql=mq.connect(
        host="localhost",
        user="phpmyadmin",
        password="Phpmy@dm1n",
        database="school"
    )

mycursor=mysql.cursor()

print("{:<15} {:<20} {:<20} {:<10}".format("Student Id","Student Name","Student Class","Student Email"))

try:

    sql = "Select * from students"

    mycursor.execute(sql)

    sdata=mycursor.fetchall()

    for x in sdata:
            print("{:<15} {:<20} {:<20} {:<10}".format(x[0],x[1],x[2],x[3]))
except:
    print("Error:-")