from pydantic import BaseModel
from ..config.db_connection import get_connection
from fastapi import HTTPException, status, Depends
from ..models.training_request_model import TrainingRequest, RequestModel
from datetime import datetime


class TrainingRequestCrud(BaseModel):
    """
    CRUD operations for Training Requests.
    Provides methods to interact with the 'training_requests' table in the database.
    """

    def get_all_requests(self):
        """
        Retrieve all training requests from the database.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            select * from ust_db.training_requests
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            return rows

        except Exception as e:
            # Raise HTTP 400 if any error occurs during query execution
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            # Ensure resources are closed properly
            if conn.open:
                cursor.close()
                conn.close()

    def get_request_by_id(self, emp_id):
        """
        Retrieve a single training request by its ID.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            select * from ust_db.training_requests where id = %s
            """

            cursor.execute(query, (emp_id,))
            row = cursor.fetchone()
            if row:
                return row
            else:
                # Raise exception if no record is found
                raise Exception("Record not found")

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            if conn.open:
                cursor.close()
                conn.close()

    def creaate_request(self, request: TrainingRequest):
        """
        Create a new training request record in the database.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            insert into ust_db.training_requests (
                employee_id, employee_name, training_title,
                training_description, requested_date,
                status, manager_id, last_updated
            )
            values (
                %s, %s, %s,
                %s, %s,
                %s, %s, %s
            )
            """
            values = (
                request.employee_id,
                request.employee_name,
                request.training_title,
                request.training_description,
                request.requested_date,
                request.status,
                request.manager_id,
                datetime.now()
            )

            cursor.execute(query, values)
            conn.commit()

            return request

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            if conn.open:
                cursor.close()
                conn.close()

    def update_request(self, emp_id, request: TrainingRequest):
        """
        Update an existing training request record by ID.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            update ust_db.training_requests set
                employee_id = %s, employee_name = %s, training_title = %s,
                training_description = %s, requested_date = %s,
                status = %s, manager_id = %s, last_updated = %s
                where id = %s
            """
            values = (
                request.employee_id,
                request.employee_name,
                request.training_title,
                request.training_description,
                request.requested_date,
                request.status,
                request.manager_id,
                datetime.now(),
                emp_id
            )

            # Ensure record exists before updating
            if TrainingRequestCrud().get_request_by_id(emp_id):
                cursor.execute(query, values)
                conn.commit()
            else:
                raise Exception("Record not found")

            return request

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            if conn.open:
                cursor.close()
                conn.close()

    def patch_request(self, emp_id, request: RequestModel):
        """
        Partially update a training request (only status field).
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            update ust_db.training_requests set
                status = %s
                where id = %s
            """

            # Ensure record exists before patching
            if TrainingRequestCrud().get_request_by_id(emp_id):
                cursor.execute(query, (request.status, emp_id))
                conn.commit()
            else:
                raise Exception("Record not found")

            return "Status updated"

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            if conn.open:
                cursor.close()
                conn.close()

    def delete_request(self, emp_id):
        """
        Delete a training request record by ID.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
            delete from ust_db.training_requests
                where id = %s
            """

            # Ensure record exists before deletion
            if TrainingRequestCrud().get_request_by_id(emp_id):
                cursor.execute(query, (emp_id,))
                conn.commit()
            else:
                raise Exception("Record not found")

            return "Record deleted"

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        finally:
            if conn.open:
                cursor.close()
                conn.close()