import pymysql as mq

try:
    conn=mq.connect(
        host="localhost",
        user="phpmyadmin",
        password="Phpmy@dm1n",
        database="school"
    )

    cursor=conn.cursor() # cursor open karna jaruri hai tab hi ap database ke query ko run kar sakte ho...

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            st_id INT AUTO_INCREMENT PRIMARY KEY,
            st_name VARCHAR(100) NOT NULL,
            st_class VARCHAR(10) NOT NULL,
            st_email VARCHAR(50) NOT NULL
        )
    ''')

    conn.commit() # commit() bhi bahut jaruri ho agar aap database mai koi bhi change karte ho to commit function run karna jaruri hai varna koi bhi data insert update or delete nahi hoga
 
    print("Table Created Successfully")

except mq.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed.")

