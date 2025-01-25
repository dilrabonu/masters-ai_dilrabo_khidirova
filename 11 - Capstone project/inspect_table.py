import sqlite3

# Connect to the database
conn = sqlite3.connect('heart_attack.db')
cursor = conn.cursor()

# Get the schema of the table
cursor.execute("PRAGMA table_info(heart_attack_data);")
columns = cursor.fetchall()

print("Columns in the table:")
for column in columns:
    print(column)

conn.close()
