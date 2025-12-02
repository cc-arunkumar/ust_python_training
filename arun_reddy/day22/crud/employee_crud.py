import pymysql
from datetime import datetime
from fastapi import HTTPException, status

# Function to establish and return a connection to the MySQL database
def get_Connection():
    try:
        return pymysql.connect(
            host="localhost",      # Database server host
            user="root",           # Database username
            password="pass@word1", # Database password
            database="ust_training_db", # Database name
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as e:
        # 500 Internal Server Error if DB connection fails
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection failed: {str(e)}"
        )

# Column headers for mapping query results
headers = ["employee_id","employee_name","training_title","training_description",
           "requested_date","status","manager_id","last_updated"]

# -----------------------------
# CREATE Employee Training Request
# -----------------------------
def create_emp(emp):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = """INSERT INTO ust_training_db.training_requests
                   (employee_id,employee_name,training_title,training_description,
                    requested_date,status,manager_id,last_updated)  
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""" 
        data = [emp.employee_id, emp.employee_name, emp.training_title,
                emp.training_description, emp.requested_date,
                emp.status, emp.manager_id, emp.last_updated]
        cursor.execute(query, data)
        conn.commit()
        # 201 Created
        return {"status": "success", "data": emp.dict()}
    except Exception as e:
        # 400 Bad Request for invalid input/insert failure
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating employee request: {str(e)}"
        )
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -----------------------------
# READ All Employee Training Requests
# -----------------------------
def get_all():
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_training_db.training_requests")
        rows = cursor.fetchall()
        if len(rows) == 0:
            # 404 Not Found if table empty
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No training requests found"
            )
        # 200 OK
        return {"status": "success", "data": rows}
    except Exception as e:
        # 500 Internal Server Error for unexpected issues
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching records: {str(e)}"
        )
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -----------------------------
# READ Employee Training Request by ID
# -----------------------------
def get_by_id(emp_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_training_db.training_requests WHERE ID=%s", (emp_id,))
        row = cursor.fetchone()
        if not row:
            # 404 Not Found if record missing
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee request with ID {emp_id} not found"
            )
        # 200 OK
        return {"status": "success", "data": row}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching record: {str(e)}"
        )
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -----------------------------
# UPDATE Employee Training Request by ID
# -----------------------------
def update_by_id(emp_id, emp):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = """UPDATE ust_training_db.training_requests 
                   SET employee_id=%s, employee_name=%s, training_title=%s, training_description=%s,
                       requested_date=%s, status=%s, manager_id=%s, last_updated=%s 
                   WHERE ID=%s"""
        data = (emp.employee_id, emp.employee_name, emp.training_title,
                emp.training_description, emp.requested_date,
                emp.status, emp.manager_id, emp.last_updated, emp_id)
        cursor.execute(query, data)
        conn.commit()
        if cursor.rowcount == 0:
            # 404 Not Found if no record updated
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee request with ID {emp_id} not found"
            )
        # 200 OK
        return {"status": "success", "data": emp.dict()}
    except Exception as e:
        # 400 Bad Request for invalid update
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error updating record: {str(e)}"
        )
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -----------------------------
# PARTIAL UPDATE (Status only)
# -----------------------------
def update_partial(emp_id, state):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = """UPDATE ust_training_db.training_requests SET status=%s WHERE ID=%s"""
        data = (state.status, emp_id)
        cursor.execute(query, data)
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee request with ID {emp_id} not found"
            )
        # 200 OK
        return get_by_id(emp_id)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error updating status: {str(e)}"
        )
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# -----------------------------
# DELETE Employee Training Request by ID
# -----------------------------
def delete_by_id(emp_id):
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ust_training_db.training_requests WHERE ID=%s", (emp_id,))
        conn.commit()
        if cursor.rowcount == 0:
            # 404 Not Found if record missing
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee request with ID {emp_id} not found"
            )
        # 200 OK
        return {"status": "success", "message": "Record deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting record: {str(e)}"
        )
    finally:
        if conn.open:
            cursor.close()
            conn.close()
