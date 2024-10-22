import sqlite3

DB_NAME = 'weather_data.db'
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

# Fetch all data from the weather table
c.execute("SELECT city, temperature, timestamp FROM weather ORDER BY timestamp DESC")
data = c.fetchall()

if data:
    print("Records in the weather table:")
    for record in data:
        print(record)
else:
    print("No records found in the weather table.")

conn.close()
