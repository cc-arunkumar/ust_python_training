from app.models import TrainingRequest, TrainingRequestCreate
from app.db_connection import get_db_connection
from fastapi import HTTPException
from typing import Optional


# Function to create a new training request in the database
def create_training_request(request: TrainingRequestCreate):
    """
    Creates a new training request in the database.
    :param request: The request data (employee_id, employee_name, etc.)
    :return: A message indicating whether the training request was created successfully.
    """
    connection = get_db_connection()  # Get a connection to the database
    with connection.cursor() as cursor:
        # Execute the SQL insert statement to add the new training request
        cursor.execute(
            "INSERT INTO training_requests (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (request.employee_id, request.employee_name, request.training_title, request.training_description, request.requested_date, request.status, request.manager_id)
        )
        connection.commit()  # Commit the changes to the database
        return {"message": "Training request created successfully."}  # Return success message


# Function to fetch all training requests, optionally filtered by status
def read_all_training_requests(status_filter: Optional[str] = ""):
    """
    Fetches all training requests, optionally filtered by status.
    :param status_filter: Optional status filter for the training requests (e.g., "approved", "pending")
    :return: A list of training requests.
    """
    try:
        conn = get_db_connection()  # Get a connection to the database
        cursor = conn.cursor()  # Create a cursor to execute SQL queries
        
        # If a status filter is provided, fetch training requests by status
        if status_filter == "":
            cursor.execute("SELECT * FROM ust_training_db.training_requests")  # Fetch all records if no filter
        else:
            cursor.execute("SELECT * FROM ust_training_db.training_requests WHERE status=%s", (status_filter,))  # Fetch by status
        
        rows = cursor.fetchall()  # Fetch all results from the query
        return rows  # Return the list of training requests
    
    except Exception as e:
        raise ValueError("Error during fetching")  # Handle any errors during database access
    finally:
        if conn:  # Ensure the connection is closed after the operation
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection


# Function to fetch a specific training request by its ID
def read_training_request_by_id(request_id: int):
    """
    Fetches a specific training request by its ID.
    :param request_id: The ID of the training request to fetch.
    :return: The training request data if found.
    :raises HTTPException: If the training request is not found.
    """
    try:
        conn = get_db_connection()  # Get a connection to the database
        cursor = conn.cursor()  # Create a cursor
        
        cursor.execute("SELECT * FROM ust_training_db.training_requests WHERE id = %s", (request_id,))  # Fetch the request by ID
        row = cursor.fetchone()  # Fetch a single result
        
        if row is None:  # If the training request is not found, raise an exception
            raise HTTPException(status_code=404, detail="Training request not found")
        
        return row  # Return the found training request
    
    except Exception as e:
        raise ValueError("Error during fetching")  # Handle any errors
    finally:
        if conn:  # Ensure the connection is closed after the operation
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection


# Function to update a training request by its ID
def update_training_request_by_id(request_id: int, update_data: TrainingRequestCreate):
    """
    Updates an existing training request in the database by its ID.
    :param request_id: The ID of the training request to update.
    :param update_data: The updated data for the training request.
    :return: A message indicating whether the update was successful.
    :raises ValueError: If the training request to update is not found.
    """
    try:
        conn = get_db_connection()  # Get a connection to the database
        cursor = conn.cursor()  # Create a cursor
        
        if read_training_request_by_id(request_id):  # Check if the training request exists
            # Execute the SQL update statement to modify the request data
            cursor.execute(
                "UPDATE ust_training_db.training_requests SET employee_id=%s, employee_name=%s, training_title=%s, training_description=%s, requested_date=%s, status=%s, manager_id=%s WHERE id=%s",
                (update_data.employee_id, update_data.employee_name, update_data.training_title, update_data.training_description, update_data.requested_date, update_data.status, update_data.manager_id, request_id)
            )
            conn.commit()  # Commit the changes to the database
            return {"message": "Training request updated successfully."}  # Return success message
        else:
            raise ValueError("Training request not found")  # If request is not found, raise error
    
    except Exception as e:
        raise ValueError("Error during update")  # Handle any errors
    finally:
        if conn:  # Ensure the connection is closed after the operation
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection


# Function to delete a training request by its ID
def delete_training_request_by_id(request_id: int):
    """
    Deletes a training request from the database by its ID.
    :param request_id: The ID of the training request to delete.
    :return: A message indicating whether the deletion was successful.
    :raises ValueError: If the training request to delete is not found.
    """
    try:
        conn = get_db_connection()  # Get a connection to the database
        cursor = conn.cursor()  # Create a cursor
        
        if read_training_request_by_id(request_id):  # Check if the training request exists
            cursor.execute("DELETE FROM ust_training_db.training_requests WHERE id = %s", (request_id,))  # Execute the delete statement
            conn.commit()  # Commit the changes to the database
            return {"message": "Training request deleted successfully."}  # Return success message
        else:
            raise ValueError("Training request not found")  # If request is not found, raise error
    
    except Exception as e:
        raise ValueError("Error during deletion")  # Handle any errors
    finally:
        if conn:  # Ensure the connection is closed after the operation
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection
