import json  # Import json module to load JSON data
from db_connection import get_mysql_connection  # Import the function to establish MySQL connection

class MySQLService:
    # Initialize the MySQLService class, which handles all MySQL operations
    def __init__(self):
        self.conn = get_mysql_connection()  # Establish a connection to the MySQL database
        self.cursor = self.conn.cursor()  # Create a cursor object to interact with the database

    # Method to create the 'employees' table in MySQL if it does not already exist
    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT PRIMARY KEY,  # Employee ID as the primary key
            name VARCHAR(50),  # Employee name with a max length of 50 characters
            department VARCHAR(30),  # Department with a max length of 30 characters
            age INT,  # Employee age as an integer
            city VARCHAR(30)  # Employee city with a max length of 30 characters
        );
        """
        self.cursor.execute(query)  # Execute the query to create the table
        self.conn.commit()  # Commit the changes to the database
        print("MySQL Table Created (if not exists).")  # Print confirmation message

    # Method to load employee data from a JSON file and insert it into MySQL
    def load_json_to_mysql(self, json_file):
        with open(json_file, "r") as f:  # Open the JSON file for reading
            employees = json.load(f)  # Load the employee data from the file

        query = """
        INSERT INTO employees (emp_id, name, department, age, city)  # Insert query for employee data
        VALUES (%s, %s, %s, %s, %s)  # Values placeholders for employee data
        ON DUPLICATE KEY UPDATE  # If emp_id already exists, update the existing row
            name = VALUES(name),  # Update name
            department = VALUES(department),  # Update department
            age = VALUES(age),  # Update age
            city = VALUES(city);  # Update city
        """

        # Iterate over each employee in the loaded data and insert into the database
        for emp in employees:
            self.cursor.execute(query, (
                emp["emp_id"], emp["name"], emp["department"], 
                emp["age"], emp["city"]
            ))

        self.conn.commit()  # Commit the changes to the database
        print("JSON Data Inserted Into MySQL Successfully.")  # Print confirmation message

    # Method to read all employee data from the 'employees' table in MySQL
    def read_employees(self):
        self.cursor.execute("SELECT * FROM employees")  # Execute the query to fetch all employees
        rows = self.cursor.fetchall()  # Fetch all rows from the query result
        print("Data Read From MySQL:", rows)  # Print the fetched data
        return rows  # Return the list of employees
