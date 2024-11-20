import sqlite3
conn = sqlite3.connect("sqlite.db")  #is line ke code se database create or connection ho jayega aur database ka name hai "sqllite"
conn.execute('''                     
    Create table student(
        st_id INT AUTO_INCREMENT PRIMARY KEY,
        st_name VARCHAR(50),
        st_class VARCHAR(10),
        st_email VARCHAR(30)

    )
''')
conn.close()


#conn.execute() ke method se aapko connection ke madad se aap database mai table create kar sakte hai...
#conn.close() is code se connection close ho jayega