import sqlite3

db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "SELECT * FROM users;"
cursor.execute(sql)

record = cursor.fetchone()
db.close()

print(record)
