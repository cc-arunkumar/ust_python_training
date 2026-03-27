from fastapi import APIRouter, HTTPException  # Import FastAPI modules
from app.models import TrainingRequestCreate, TrainingRequestOut  # Import Pydantic models for validation
from app.db_connection import get_db_connection  # Import helper function for DB connection

# Create an APIRouter instance to handle API routes
router = APIRouter()

# POST route: Create a new training request
@router.post("/", response_model=TrainingRequestOut)
async def create_training_request(request: TrainingRequestCreate):
    with get_db_connection() as connection:  # Establish DB connection
        cursor = connection.cursor()  # Create a cursor to execute queries
        query = """
            INSERT INTO training_requests (employee_id, employee_name, training_title, 
            training_description, requested_date, status, manager_id) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            request.employee_id,
            request.employee_name,
            request.training_title,
            request.training_description,
            request.requested_date,
            request.status,
            request.manager_id
        )
        cursor.execute(query, values)  # Execute query to insert new training request
        connection.commit()  # Commit the changes to the database
        return {**request.dict(), "id": cursor.lastrowid}  # Return the new training request with its ID

# GET route: Retrieve all training requests
@router.get("/", response_model=TrainingRequestOut)
async def get_all_training_requests():
    try:
        with get_db_connection() as connection:  # Establish DB connection
            cursor = connection.cursor()  # Create a cursor to execute queries
            query = "SELECT * FROM training_requests"  # Query to fetch all requests
            cursor.execute(query)  # Execute query
            result = cursor.fetchall()  # Fetch all results
            return result  # Return the list of training requests
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")  # Handle errors

# GET route: Retrieve a training request by ID
@router.get("/{id}", response_model=TrainingRequestOut)
async def get_training_request(id: int):
    with get_db_connection() as connection:  # Establish DB connection
        cursor = connection.cursor()  # Create a cursor to execute queries
        query = "SELECT * FROM training_requests WHERE id = %s"  # Query to fetch request by ID
        cursor.execute(query, (id,))  # Execute query with ID
        result = cursor.fetchone()  # Fetch the result
        if result is None:
            raise HTTPException(status_code=404, detail="Training request not found")  # Handle not found
        return result  # Return the training request

# DELETE route: Delete a training request by ID
@router.delete("/{id}")
async def delete_training_request(id: int):
    with get_db_connection() as connection:  # Establish DB connection
        cursor = connection.cursor()  # Create a cursor to execute queries
        query = "DELETE FROM training_requests WHERE id = %s"  # Query to delete request by ID
        cursor.execute(query, (id,))  # Execute query with ID
        connection.commit()  # Commit the changes
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Training request not found")  # Handle not found
        return {"message": "Training request deleted successfully"}  # Return success message

# PUT route: Update a training request by ID
@router.put("/{id}", response_model=TrainingRequestOut)
async def update_training_request(id: int, request: TrainingRequestCreate):
    with get_db_connection() as connection:  # Establish DB connection
        cursor = connection.cursor()  # Create a cursor to execute queries
        query = """
            UPDATE training_requests 
            SET employee_id = %s, employee_name = %s, training_title = %s, 
                training_description = %s, requested_date = %s, status = %s, manager_id = %s
            WHERE id = %s
        """
        values = (
            request.employee_id,
            request.employee_name,
            request.training_title,
            request.training_description,
            request.requested_date,
            request.status,
            request.manager_id,
            id
        )
        cursor.execute(query, values)  # Execute the query with updated data
        connection.commit()  # Commit the changes
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Training request not found")  # Handle not found
        return {**request.dict(), "id": id}  # Return updated request with ID
