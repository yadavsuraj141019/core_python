import sqlite3
conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM student")
for a in data:
    print(a)


print()

data = conn.execute("SELECT * FROM student Where st_name='Suraj'")
for n in data:
    print(n)

# aapke database mai bahut sara data ho aur aap particular name se data fetch ya search karna chhate ho like suraj to
# upar vala example dekh lo...