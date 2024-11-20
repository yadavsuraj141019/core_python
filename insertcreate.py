import pymysql as mq

mysql=mq.connect(
        host="localhost",
        user="phpmyadmin",
        password="Phpmy@dm1n",
        database="school"
    )

mycursor=mysql.cursor()

try:
    ins="INSERT INTO students (st_name,st_class,st_email) VALUES (%s,%s,%s)"

    t=[("Aj",'11th',"aj@gmail.com"),("Vicky",'10th',"vicky@gmail.com")]  
    mycursor.executemany(ins,t) # aap ko query likh die to uske bad usko execute karna comulsory hai varna query run nhi hoga....
    mysql.commit()
    print("INSERT DATA INTO TABLE STUDENTS:-")
except:
    print("Error:-")