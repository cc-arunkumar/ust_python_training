import pymysql   # PyMySQL library used for MySQL database connectivity

def get_connection():
    try:
        # Attempt to establish a database connection
        connection = pymysql.connect(
            host="localhost",                        # MySQL server hostname
            user="root",                             # Database username
            password="pass@word1",                   # Database password (use env vars in production)
            database="aims_plus",                 # Target database name
            port=3306,                               # Default MySQL port
            cursorclass=pymysql.cursors.DictCursor   # Fetch rows as dictionaries instead of tuples
        )
        return connection
    except pymysql.MySQLError as e:
        # Handle and log any MySQL-related connection errors
        print(f"Database connection error: {e}")   # Replace print with proper logging in production
        return None
