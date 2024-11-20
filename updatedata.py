import sqlite3
conn = sqlite3.connect("sqlite.db")
conn.execute('''
    UPDATE student SET st_name = "Heyansh" where st_id=1
''')
conn.commit()
conn.close()