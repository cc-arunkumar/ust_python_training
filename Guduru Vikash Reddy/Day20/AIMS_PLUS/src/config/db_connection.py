# Importing the necessary libraries
import pymysql  # pymysql is a library used to interact with MySQL databases
from src.exceptions.custom_exceptions import DatabaseConnectionException  # Custom exception for handling database connection errors


def get_connection():
    """
    Function to establish a connection to the MySQL database.
    
    Returns:
        conn (pymysql.Connection): Returns the connection object if successful.
    
    Raises:
        DatabaseConnectionException: Raises a custom exception if the database connection fails.
    """
    try:
        # Attempting to establish a connection to the database
        conn = pymysql.connect(
            host="localhost",  # Database host (localhost for local development)
            user="root",  # Database username (root by default)
            password="pass@word1",  # Database password (should be replaced with actual secure password)
            database="ust_aims_db",  # The specific database to connect to
            cursorclass=pymysql.cursors.DictCursor  # Using DictCursor to return results as dictionaries
        )
        return conn  # If successful, return the connection object

    except DatabaseConnectionException as e:
        # If a custom database connection exception is raised, handle it here
        print("Error:", e)  # Print the error message for debugging purposes
