import sqlite3
conn = sqlite3.connect("sqlite.db")
st_id = input("Enter Student Id:")
conn.execute("DELETE FROM student Where st_id="+st_id)
conn.commit()
conn.close()
