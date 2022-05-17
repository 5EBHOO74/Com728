import sqlite3

print("Please enter the user's name")
name = input()

print("Please enter the user's height (m)")
height = float(input())

print("Please enter the user's weight (kg)")
weight = float(input())

print("Please enter the user's date of birth")
date_of_birth = input()

db = sqlite3.connect("users.db")
cursor = db.cursor()

sql = "INSERT INTO users " \
       "(name, height, weight, date_of_birth) " \
       "VALUES " \
       "(?, ?, ?, ?, ?);"
values = [name, height, weight, date_of_birth]
cursor.execute(sql, values)
row_id = cursor.lastrowid
db.close()

print("The record has been added to the database.")
print(f"Id of new record is {row_id}")