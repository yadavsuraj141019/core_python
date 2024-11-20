import sqlite3
conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM student")
for a in data:
    print(a)



# upar vala example se aur select query ke madad se database ka data aap fetch kar sakte ho....


# aapke database mai bahut sare data hai like 20 data hai par aapko 20 data nahi dikhana hai bas 2 data ya 5 data
# dikhana hai to limit ka used hota hai like limit 0,2 iska matlab 1 aur 2 data dikhega agar aapko 4 se data
# dikhana to aapko likhna padega like limit 5,2 aur isme jo 5 ke bad 2 likha uska matlab hota 2 data
# dikhana agar 3 data dikhana hai to 3 likh do...


