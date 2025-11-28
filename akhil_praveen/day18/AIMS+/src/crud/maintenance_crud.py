import pymysql
from typing import Optional
from ..models.maintenance_model import MaintenanceLog, StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv

# Function to retrieve column names from the maintenance_log table
def get_keys():
    try:
        conn = get_connection()  # Establish the database connection
        cursor = conn.cursor()
        
        # Query to fetch the column names of the maintenance_log table
        cursor.execute("""SELECT COLUMN_NAME
                          FROM INFORMATION_SCHEMA.COLUMNS
                          WHERE TABLE_SCHEMA = 'ust_aims_plus'
                          AND TABLE_NAME = 'maintenance_log'
                          ORDER BY ORDINAL_POSITION;""")
        col = cursor.fetchall()
        keys = []
        
        # Append each column name to the keys list
        for i in col:
            keys.append(i[0])
        return keys  # Return the list of column names
    except Exception as e:
        raise
    finally:
        # Close the database connection and cursor
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed!")

# Class for performing CRUD operations on maintenance log data in the database
class MaintenanceCrud:
    
    # Method to insert a new maintenance log record into the database
    def create_maintenance(self, data: MaintenanceLog):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to insert new maintenance log data
            query = """
            insert into ust_aims_plus.maintenance_log (asset_tag, maintenance_type, vendor_name, description,
            cost, maintenance_date, technician_name, status) 
            values (%s, %s, %s, %s,
            %s, %s, %s, %s)
            """
            values = tuple(data.__dict__.values())  # Convert the data object to a tuple
            cursor.execute(query, values)  # Execute the insertion query
            conn.commit()  # Commit the transaction to save changes
            print("Data added successfully!")
            return data  # Return the newly created maintenance log data
            
        except Exception as e:
            print(e)
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to retrieve all maintenance logs, or filter by status
    def get_all_maintenance(self, status):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the maintenance_log table
            keys = get_keys()
            
            # Query to retrieve maintenance logs based on the provided status
            if status == "ALL":
                query = """select * from ust_aims_plus.maintenance_log"""
                cursor.execute(query)
            else:
                query = """select * from ust_aims_plus.maintenance_log where status = %s"""
                cursor.execute(query, (status,))
            
            rows = cursor.fetchall()  # Fetch all the rows from the executed query
            if rows:
                list_rows = []
                # Convert each row to a dictionary using the column names as keys
                for values in rows:
                    list_rows.append(dict(zip(keys, values)))
                return list_rows  # Return the list of maintenance logs
            else:
                return None  # Return None if no rows are found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to retrieve a maintenance log by its log ID
    def get_maintenance_by_id(self, log_id):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the maintenance_log table
            keys = get_keys()
            query = """select * from ust_aims_plus.maintenance_log where log_id = %s"""
            cursor.execute(query, (log_id,))
            row = cursor.fetchone()  # Fetch a single row by log ID
            if row:
                list_rows = [dict(zip(keys, row))]  # Convert the row into a dictionary
                return list_rows  # Return the found maintenance log data
            else:
                raise  # Raise an exception if maintenance log is not found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to update an existing maintenance log record by log ID
    def update_maintenance(self, id, data: MaintenanceLog):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to update the maintenance log data by log ID
            query = """
            update ust_aims_plus.maintenance_log set asset_tag=%s, maintenance_type=%s, vendor_name=%s, description=%s,
            cost=%s, maintenance_date=%s, technician_name=%s, status=%s where log_id=%s
            """
            values = tuple(data.__dict__.values()) + (id,)  # Append the log ID to the values tuple
            cursor.execute(query, values)  # Execute the update query
            conn.commit()  # Commit the transaction to save the changes
            print("Data updated successfully!")
            return data  # Return the updated maintenance log data
            
        except Exception as e:
            print(str(e))
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to update the status of a maintenance log by its log ID
    def update_maintenance_status(self, id, status):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to update the maintenance log status
            query = """update ust_aims_plus.maintenance_log set status=%s where log_id=%s"""
            values = (status, id)  # Set the status and log ID
            cursor.execute(query, values)  # Execute the update query
            conn.commit()  # Commit the transaction to save the changes
            print("Status updated!")
            return self.get_maintenance_by_id(id)  # Return the updated maintenance log data
                
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to delete a maintenance log record by log ID
    def delete_maintenance(self, id):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            condition = self.get_maintenance_by_id(id)  # Check if the maintenance log exists
            if condition:
                # Query to delete the maintenance log by its log ID
                query = """delete from ust_aims_plus.maintenance_log where log_id=%s"""
                values = (id,)  # Set the log ID to be deleted
                cursor.execute(query, values)  # Execute the delete query
                conn.commit()  # Commit the transaction to delete the maintenance log
                print("Maintenance deleted from id =", id)
                keys = get_keys()
                list_rows = [dict(zip(keys, condition))]  # Convert the deleted log data to a dictionary
                return list_rows  # Return the deleted maintenance log data
                
            else:
                raise  # Raise exception if maintenance log is not found
                
        except Exception as e:
            print(e)
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to search for maintenance logs by a specific keyword and value
    def get_maintenance_by_keyword(self, keyword, value):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the maintenance_log table
            keys = get_keys()
            
            # Construct the query to search for maintenance logs by the given keyword
            query = f"""select * from ust_aims_plus.maintenance_log where {keyword}=%s"""
            cursor.execute(query, (value,))
            rows = cursor.fetchall()  # Fetch all matching rows
            if rows:
                list_rows = []
                # Convert each row into a dictionary
                for values in rows:
                    list_rows.append(dict(zip(keys, values)))
                return list_rows  # Return the matched maintenance logs
            else:
                raise  # Raise exception if no maintenance logs are found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to get the total count of maintenance logs in the maintenance_log table
    def get_all_maintenance_count(self):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            query = """select * from ust_aims_plus.maintenance_log"""
            cursor.execute(query)
            rows = cursor.fetchall()  # Fetch all rows
            if rows:
                return len(rows)  # Return the count of rows (maintenance logs)
            else:
                return None  # Return None if no maintenance logs are found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    
    # Method to bulk upload maintenance from a CSV file     
    def bluk_upload(self):
        try:
            with open("path/to/maintenance_log.csv","r") as maintenance_file:
                csv_file = csv.DictReader(maintenance_file)
                for data in csv_file:
                    self.create_maintenance(data)
        except Exception as e:
            return e
