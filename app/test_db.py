import sqlite3

# connect to your database
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# run a query to see all todos
cursor.execute("SELECT * FROM todos")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()