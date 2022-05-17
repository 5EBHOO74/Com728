import sqlite3

db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "SELECT * FROM users;"
cursor.execute(sql)

records = cursor.fetchall()
db.close()

print("All users in the system:")

for record in records:
    print(record)