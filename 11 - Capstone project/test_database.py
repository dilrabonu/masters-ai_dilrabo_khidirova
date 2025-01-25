import sqlite3

conn = sqlite3.connect('heart_attack.db')
cursor = conn.cursor()

# Check table existence
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Check row count
cursor.execute("SELECT COUNT(*) FROM heart_attack_data;")
print("Row count:", cursor.fetchone())

# View sample data
cursor.execute("SELECT * FROM heart_attack_data LIMIT 5;")
print("Sample data:", cursor.fetchall())

conn.close()
