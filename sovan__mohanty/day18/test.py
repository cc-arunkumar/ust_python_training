import pymysql

# Connect to MySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_db"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query (replace 'your_table' with the actual table name)
cursor.execute("SELECT * FROM emp")

# Fetch all rows
rows = cursor.fetchall()

# Print results
print("Data from ust_db.emp:")
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()
