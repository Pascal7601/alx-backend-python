import sqlite3
import csv

conn = sqlite3.connect("airbnb.db")
cursor = conn.cursor()
with open('user_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name, email, age = row["name"], row["email"], row["age"]
        cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))

conn.commit()
cursor.close()