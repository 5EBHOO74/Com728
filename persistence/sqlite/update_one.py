import sqlite3

print("Please enter the user id:")
id = int(input())

db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "SELECT * FROM users WHERE id=?"
values = [id]
cursor.execute(sql, values)
record = cursor.fetchone()
db.close()

print("Current user details are as follows:")
print(f"id: {record[0], height(m): {record[1]}, weight(kg): {record[2]}, date of birth: {record[3]}")

print("What would you like to change?")
field = input()

print(f"What is the new value for {field}?")
value = input()

db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = f"UPDATE users SET {data[0]}=? WHERE id=?"
values = [data[1], id]
cursor.execute(sql, values)
db.commit()
db.close()

print("The record has been updated.")
