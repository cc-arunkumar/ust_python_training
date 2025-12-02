from models import TrainingRequest, TrainingRequestCreate, TrainingRequestUpdate
from db_connection import get_connection  
from fastapi import HTTPException

def create_training_request(request: TrainingRequestCreate):
    """
    Create a new training request in the database.
    This function takes in a TrainingRequestCreate Pydantic model, inserts it into the 
    database, and returns the newly created record.

    Args:
        request (TrainingRequestCreate): Pydantic model containing the data to insert.

    Returns:
        dict: The newly created training request, or raises an exception in case of an error.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """INSERT INTO training_requests 
                   (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                (
                    request.employee_id,
                    request.employee_name,
                    request.training_title,
                    request.training_description,
                    request.requested_date,
                    request.status,
                    request.manager_id,
                ),
            )
            connection.commit()  # Commit the transaction to save the record in the DB.
            new_id = cursor.lastrowid  # Get the last inserted row's ID.
            
            # Fetch the newly created training request to return it as a dictionary.
            cursor.execute("SELECT * FROM training_requests WHERE id=%s", (new_id,))
            return cursor.fetchone()  # Return the created record.
    except Exception as e:
        # If an exception occurs (e.g., DB error), rollback and raise an HTTPException.
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating request: {str(e)}")
    finally:
        connection.close()  # Always close the connection after the operation.

def get_all_training_requests():
    """
    Fetch all training requests from the database.
    This function retrieves all training request records from the DB.

    Returns:
        list: A list of all training requests or an empty list if no records exist.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM training_requests")
            return cursor.fetchall()  # Return all records.
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching records: {str(e)}")
    finally:
        connection.close()

def get_training_request_by_id(request_id: int):
    """
    Fetch a single training request by its ID.
    This function fetches the training request that matches the given ID.
    
    Args:
        request_id (int): The ID of the training request to fetch.

    Returns:
        dict: The training request matching the given ID.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM training_requests WHERE id=%s", (request_id,))
            row = cursor.fetchone()
            if not row:
                # Raise a 404 error if no request with the given ID is found.
                raise HTTPException(status_code=404, detail=f"Training request with ID {request_id} not found")
            return row  # Return the found record.
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching the record: {str(e)}")
    finally:
        connection.close()

def update_training_request(request_id: int, request: TrainingRequestCreate):
    """
    Update a training request by its ID.
    This function updates an existing training request's details based on the provided ID.
    
    Args:
        request_id (int): The ID of the training request to update.
        request (TrainingRequestCreate): Pydantic model with updated data.
    
    Returns:
        dict: The updated training request, or raises an exception if not found.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM training_requests WHERE id=%s", (request_id,))
            if not cursor.fetchone():
                # If the request does not exist, raise a 404 error.
                raise HTTPException(status_code=404, detail="Training request not found")

            cursor.execute(
                """UPDATE training_requests SET 
                   employee_id=%s, employee_name=%s, training_title=%s, training_description=%s,
                   requested_date=%s, status=%s, manager_id=%s
                   WHERE id=%s""",
                (
                    request.employee_id,
                    request.employee_name,
                    request.training_title,
                    request.training_description,
                    request.requested_date,
                    request.status,
                    request.manager_id,
                    request_id,
                ),
            )
            connection.commit()  # Commit the changes to the database.
            cursor.execute("SELECT * FROM training_requests WHERE id=%s", (request_id,))
            return cursor.fetchone()  # Return the updated record.
    except Exception as e:
        connection.rollback()  # Rollback the transaction in case of an error.
        raise HTTPException(status_code=500, detail=f"Error updating request: {str(e)}")
    finally:
        connection.close()

def patch_training_request(request_id: int, request: TrainingRequestUpdate):
    """
    Partially update a training request by its ID.
    This function updates only the fields provided in the request (i.e., partial update).
    
    Args:
        request_id (int): The ID of the training request to update.
        request (TrainingRequestUpdate): Pydantic model with fields to update.

    Returns:
        dict: The updated training request, or raises an exception if not found.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM training_requests WHERE id=%s", (request_id,))
            if not cursor.fetchone():
                # If the request does not exist, raise a 404 error.
                raise HTTPException(status_code=404, detail="Training request not found")

            # Dynamically build the SQL update query with only the provided fields.
            fields = []
            values = []
            for name, value in request.model_dump(exclude_unset=True).items():
                fields.append(f"{name}=%s")
                values.append(value)

            if not fields:
                # If no fields are provided, return the existing record without making changes.
                cursor.execute("SELECT * FROM training_requests WHERE id=%s", (request_id,))
                return cursor.fetchone()

            sql = f"UPDATE training_requests SET {', '.join(fields)} WHERE id=%s"
            values.append(request_id)
            cursor.execute(sql, tuple(values))
            connection.commit()  # Commit the changes to the database.

            cursor.execute("SELECT * FROM training_requests WHERE id=%s", (request_id,))
            return cursor.fetchone()  # Return the updated record.
    except Exception as e:
        connection.rollback()  # Rollback the transaction in case of an error.
        raise HTTPException(status_code=500, detail=f"Error patching request: {str(e)}")
    finally:
        connection.close()

def delete_training_request(request_id: int):
    """
    Delete a training request by its ID.
    This function deletes the training request that matches the given ID.
    
    Args:
        request_id (int): The ID of the training request to delete.
    
    Returns:
        dict: A success message confirming the deletion, or raises an error if not found.
    """
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM training_requests WHERE id=%s", (request_id,))
            if not cursor.fetchone():
                # If the request does not exist, raise a 404 error.
                raise HTTPException(status_code=404, detail="Request not found")

            cursor.execute("DELETE FROM training_requests WHERE id=%s", (request_id,))
            connection.commit()  # Commit the deletion to the database.
            return {"message": "Training request deleted successfully"}
    except Exception as e:
        connection.rollback()  # Rollback in case of an error.
        raise HTTPException(status_code=500, detail=f"Error deleting request: {str(e)}")
    finally:
        connection.close()

