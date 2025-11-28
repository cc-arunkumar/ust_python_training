import csv
from fastapi import HTTPException, status
from ..config import db_connection

# Define headers for employee fields
headers = ["emp_code","full_name","email","phone","department","location","join_date","status"]

# Function to get all employees or filter by status
def get_all(status):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_aims_plus.employee_directory")
        rows = cursor.fetchall()

        if not rows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No employees found")

        response = []
        if status == "":
            for row in rows:
                response.append(dict(zip(headers, row)))
            return response
        if status == "count":
            return {"count": len(rows)}
        else:
            for row in rows:
                if row[7] == status:  # status field
                    response.append(dict(zip(headers, row)))
            return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to get employee by ID
def get_by_id(emp_id):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_aims_plus.employee_directory WHERE EMP_ID=%s", (emp_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        return dict(zip(headers, row))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to create a single employee record
def create_asset(row):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ust_aims_plus.employee_directory(
            emp_code,full_name,email,phone,department,
            location,join_date,status
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        data = (
            row.emp_code, row.full_name, row.email, row.phone,
            row.department, row.location, row.join_date, row.status
        )
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Employee record inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update employee record by ID
def update_by_id(emp_id, row):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = """ 
        UPDATE ust_aims_plus.employee_directory SET emp_code=%s,full_name=%s,email=%s,phone=%s,
        department=%s,location=%s,join_date=%s,status=%s
        WHERE EMP_ID=%s"""
        data = (
            row.emp_code, row.full_name, row.email, row.phone,
            row.department, row.location, row.join_date, row.status, emp_id
        )
        cursor.execute(query, data)
        conn.commit()
        return {"message": "Employee updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to update employee status by ID
def update_by_status(emp_id, status):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = "UPDATE ust_aims_plus.employee_directory SET status=%s WHERE EMP_ID=%s"
        cursor.execute(query, (status, emp_id))
        conn.commit()
        return get_by_id(emp_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to delete employee record by ID
def delete_by_id(emp_id):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        query = "DELETE FROM ust_aims_plus.employee_directory WHERE EMP_ID=%s"
        cursor.execute(query, (emp_id,))
        conn.commit()
        return {"message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to search employees by field and keyword
def get_by_search(field_type, keyword):
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM ust_aims_plus.employee_directory WHERE {field_type} LIKE %s", (f'%{keyword}%',))
        rows = cursor.fetchall()
        if not rows:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No matching employees found")
        return [dict(zip(headers, row)) for row in rows]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to get count of all employees
def get_by_count():
    try:
        return {"count": len(get_all(""))}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Function to get employees filtered by status
def get_assets_by_status(status):
    return get_all(status)

