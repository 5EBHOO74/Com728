import csv
import sqlite3

print("Please enter a file path:")
file_path = input()

data = []
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        data.append(line)

print("Inserting data in to database...")

db = sqlite3.connect("users.db")
cursor = db.cursor()

for item in data:
    sql = "INSERT INTO users " \
          "(name, height, weight, date_of_birth)" \
          "VALUES" \
          "(?, ?, ?, ?, ?)"
    values = [item[0], item[1], item[2], item[3]]
    cursor.execute(sql, values)

db.commit()
db.close()

print(f"Done! {len(data)} records inserted.")