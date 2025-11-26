import pymysql   # PyMySQL library used for MySQL database connectivity

def get_connection():
    # Function to create and return a MySQL database connection
    try:
        # Attempt to establish a database connection
        return pymysql.connect(
            host="localhost",                   # MySQL server hostname
            user="root",                        # Database username
            password="pass@word1",              # Database password (should be secured via environment variables in production)
            database="ust_asset_db",            # Target database name
            cursorclass=pymysql.cursors.DictCursor  # Fetch rows as dictionaries instead of tuples
        )
    except pymysql.MySQLError as e:
        # Handle and log any MySQL-related connection errors
        print(f"Database connection error: {e}")   # In production, replace print with proper logging
        
        # Return None to indicate the connection attempt failed
        return None
