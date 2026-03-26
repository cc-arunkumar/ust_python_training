from config.db_connection import get_connection

print("Trying to connect to database...")

try:
    conn = get_connection()
    print("Database connection successful:", conn)
    conn.close()
except Exception as e:
    print("Database connection failed:", e)
