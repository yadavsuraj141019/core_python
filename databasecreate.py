import pymysql as mq

try:
    # Connect to the database
    myobj = mq.connect(
        host="localhost",
        user="phpmyadmin",
        password="Phpmy@dm1n",
        database="school"  # Adjust as necessary
    )
    print("Connection successful!")
    
    # You can perform database operations here

except mq.MySQLError as e:
    print(f"Error connecting to the database: {e}")


finally:
    if 'myobj' in locals() and myobj.open:
        myobj.close()

