from db_connection import get_mysql_connection  # Importing the database connection function
import json  # Importing the JSON module to work with JSON data

# Function to load data from a JSON file and insert into MySQL
def load_json_to_mysql():
    
    # Open the JSON file and load its content
    with open("employees.json", "r") as file:
        data = json.load(file)
        
    # Establish a database connection
    conn = get_mysql_connection()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        # Iterate through each employee in the JSON data
        for emp in data:
            # Insert or update employee data in the MySQL table
            cursor.execute("""
                            INSERT INTO employees (emp_id, name, department, age, city)
                            VALUES (%s, %s, %s, %s, %s)
                            ON DUPLICATE KEY UPDATE emp_id=emp_id
                        """, (emp['emp_id'], emp['name'], emp['department'], emp['age'], emp['city']))
            
        # Commit the transaction to save changes
        conn.commit()
    except Exception as e:
        # Raise an error if any exception occurs during the insertion process
        raise ValueError("Error while inserting", e)

    finally:
        # Close the cursor and connection to the database
        cursor.close()
        conn.close()

# Function to read employee data from MySQL and print it
def read_data_from_mysql():
    try:
        # Establish a database connection
        conn = get_mysql_connection()
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Execute a SELECT query to fetch all employee records
        cursor.execute("SELECT * FROM ust_mysql_db.employees")

        # Fetch all rows of the query result
        employess = cursor.fetchall()
        
        # Print each employee record
        for emp in employess:
            print(emp)
    
    except Exception as e:
        # Raise an error if unable to retrieve data
        raise ValueError("Unable to get data from database", e)
    
    finally:
        # Close the cursor and connection to the database
        cursor.close()
        conn.close()

# Function to modify data retrieved from MySQL (e.g., adding a category)
def modify_data_from_mysql():
    try:
        # Establish a database connection
        conn = get_mysql_connection()

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Execute a SELECT query to fetch all employee records
        cursor.execute("SELECT * FROM ust_mysql_db.employees")
        
        # Fetch all rows of the query result
        emp_data = cursor.fetchall()
        
        # List to hold the modified employee data
        modify_data = []
        
        # Iterate through each employee and add a 'category' based on their age
        for emp in emp_data:
            category = "Fresher" if emp["age"] < 25 else "Experienced"
            
            # Add the 'category' field to the employee data
            emp["category"] = category
            
            # Append the modified employee data to the list
            modify_data.append(emp)
        
    except Exception as e:
        # Raise an error if unable to modify the data
        raise ValueError("Unable to modify the data")
    
    finally:
        # Close the cursor and connection to the database
        cursor.close()
        conn.close()
        
    # Return the modified employee data
    return modify_data
