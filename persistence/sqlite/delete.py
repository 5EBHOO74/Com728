import sqlite3


print("Please enter the user id:")
id = int(input())

db = sqlite3.connect("users.db")
cursor = db.cursor()values = [id]
sql = "SELECT * FROM users WHERE id=?"
cursor.execute(sql, values)
record = cursor.fetchone()

print(f"The following record has been found:")
print(f"id: {record[0], height(m): {record[1]}, weight(kg): {record[2]}, date of birth: {record[3]}")


sql = "DELETE FROM users WHERE id=?"
cursor.execute(sql, values)
db.commit()
db.close()

print("The record has been removed.")