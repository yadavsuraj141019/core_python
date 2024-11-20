import sqlite3
conn = sqlite3.connect("sqlite.db")
ins = '''
    insert into student (st_name, st_class, st_email) VALUES ("Vicky1","B.C.A","vicky1@gmail.com")

'''
conn.execute(ins)
conn.commit()
conn.close()


# upar vale example se apne database mai data insert kara sakte hai.......