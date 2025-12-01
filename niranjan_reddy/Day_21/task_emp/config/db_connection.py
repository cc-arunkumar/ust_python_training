import pymysql  # Importing the pymysql library for database connection

# Function to establish a connection to the MySQL database
def get_connection():
    # Establishing a connection to the MySQL database with the specified parameters
    conn = pymysql.connect(
        host='localhost',  # The host where the MySQL server is running (localhost in this case)
        user='root',  # The MySQL username
        password='pass@word1',  # The password for the MySQL user
        database='ust_emp_db',  # The name of the database to connect to
        cursorclass=pymysql.cursors.DictCursor  # Using a dictionary cursor to return query results as dictionaries
    )
    return conn  # Returning the established connection object
