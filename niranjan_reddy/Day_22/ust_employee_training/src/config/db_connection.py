import pymysql

# Function to establish a connection to the MySQL database
def get_connection():
    try:
        # Attempt to create a connection to the MySQL database
        conn = pymysql.connect(
            host='localhost',  # Host where the database is located (localhost for local development)
            user='root',       # Database username (root user in this case)
            password='1234',  # Password for the database user
            database='ust_training_db',  # The database to connect to
            cursorclass=pymysql.cursors.DictCursor  # To return results as dictionaries (key-value pairs)
        )
        
        return conn  # Return the connection object if successful
    
    except Exception as e:
        # If an error occurs during the connection attempt, print the error message
        print("Error:", e)  # Log the exception message
