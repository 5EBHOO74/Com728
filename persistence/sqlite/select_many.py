import sqlite3

db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "SELECT * FROM users;"
cursor.execute(sql)

num_records = input("How many records?")

if num_records == "":
    records = cursor.fetchall()
else:
    records = cursor.fetchmany(int(num_records))

db.close()

print(f"First {num_records} users in the system:")

for record in records:
    print(record)

