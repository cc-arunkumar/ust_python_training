from src.config.db_connection import get_connection
from src.models.training_request_model import TrainingRequest

# Function to retrieve all training request data from the database
def get_data():
    try:
        # Establish a connection to the database
        conn = get_connection()
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Execute the SQL query to fetch all records from the training_requests table
        cursor.execute("SELECT * FROM ust_training_db.training_requests;")
        
        # Fetch all rows from the executed query
        rows = cursor.fetchall()
        
        return rows  # Return the fetched data
    
    except:
        # If any error occurs, raise a ValueError with a message
        raise ValueError("Unable to get the data")
    
    finally:
        # Close the cursor and connection to the database
        cursor.close()
        conn.close()
        
# Function to retrieve a specific training request by ID
def get_data_by_id(id):
    try:
        # Establish a connection to the database
        conn = get_connection()
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Execute the SQL query to fetch a record by ID
        cursor.execute("SELECT * FROM ust_training_db.training_requests WHERE id=%s", (id,))
        
        # Fetch the single record returned by the query
        row = cursor.fetchone()
        
        return row  # Return the fetched record
    
    except:
        # If any error occurs, raise a ValueError with a message
        raise ValueError("Unable to get the data by id")
    
    finally:
        # Close the cursor and connection to the database
        cursor.close()
        conn.close()

# Function to insert new training request data into the database
def insert_to_db(new_data):
    try:
        # Establish a connection to the database
        conn = get_connection()
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Execute the SQL INSERT statement with the new data
        cursor.execute("""
            INSERT INTO ust_training_db.training_requests (
                employee_id, employee_name, training_title, training_description,
                requested_date, status, manager_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            new_data.employee_id, new_data.employee_name, new_data.training_title,
            new_data.training_description, new_data.requested_date, new_data.status, new_data.manager_id
        ))

        # Commit the transaction to persist the data in the database
        conn.commit()

    except Exception as e:
        # If any error occurs, raise a ValueError with the error message
        raise ValueError(f"Error: {e}")
    
    finally:
        # Clean up by closing the cursor and connection
        cursor.close()
        conn.close()

# Function to update an existing training request by its ID
def update_db(id: int, update_data: TrainingRequest):
    try:
        # Establish a connection to the database
        conn = get_connection()
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Execute the SQL UPDATE statement with the provided data
        cursor.execute("""
            UPDATE ust_training_db.training_requests SET 
            employee_id=%s, employee_name=%s, training_title=%s,
            training_description=%s, requested_date=%s, status=%s, manager_id=%s WHERE id=%s
        """, (
            update_data.employee_id,
            update_data.employee_name,
            update_data.training_title,
            update_data.training_description,
            update_data.requested_date,
            update_data.status, 
            update_data.manager_id, 
            id
        ))

        # Commit the transaction to apply the changes
        conn.commit()
        
        return {"detail": "Record updated successfully"}  # Return success message
        
    except Exception as e:
        # If any error occurs, raise a ValueError with the error message
        raise ValueError(f"Unable to update the data: {e}")
    
    finally:
        # Clean up by closing the cursor and connection
        cursor.close()
        conn.close()

# Function to delete a training request by its ID
def delete_row(id):
    try:
        # Establish a connection to the database
        conn = get_connection()
        
        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()
        
        # Execute the SQL DELETE statement to remove the record by ID
        cursor.execute("DELETE FROM ust_training_db.training_requests WHERE id=%s", (id,))
        
        # Commit the transaction to apply the changes
        conn.commit()
        
        return {"detail": "Record deleted successfully"}  # Return success message
    
    except:
        # If any error occurs, raise a ValueError with a message
        raise ValueError("Unable to delete the record")
    
    finally:
        # Clean up by closing the cursor and connection
        cursor.close()
        conn.close()
