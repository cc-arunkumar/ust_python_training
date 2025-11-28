# Import database connection configuration
from ..config import db_connection
import csv
from fastapi import HTTPException, status
from ..exceptions.custom_exceptions import DatabaseConnectionException
from datetime import datetime, date

# Function to insert asset records from CSV into database
def create_assets():
    try:
        # Establish database connection
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        
        # SQL query for inserting asset records
        query = """
        INSERT INTO ust_aims_plus.asset_inventory(
            asset_tag, asset_type, serial_number,
            manufacturer, model, purchase_date, 
            warranty_years, condition_status, assigned_to,
            location, asset_status, last_updated
        ) VALUES (%s,%s,%s,
        %s,%s,%s,
        %s,%s,%s,
        %s,%s,NOW())
        """
        
        # Open asset CSV file
        with open("C:/Users/Administrator/Desktop/AIMS_update/database/sampledata/final_data/validated_asset_inventory.csv", "r") as file:
            content = csv.DictReader(file)
            
            # Loop through each row in CSV
            for row in content:
                try:
                    # Prepare data tuple for insertion
                    data = (
                        row["asset_tag"], row["asset_type"], row["serial_number"],
                        row["manufacturer"], row["model"], row["purchase_date"],
                        row["warranty_years"], row["condition_status"], row["assigned_to"],
                        row["location"], row["asset_status"], datetime.now()
                    )
                    # Execute SQL insert
                    cursor.execute(query, data)
                except Exception as e:
                    # Handle invalid row data
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Invalid row data: {e}"
                    )
        # Commit transaction
        conn.commit()
        return {"message": "Asset records inserted successfully"}
    except DatabaseConnectionException as e:
        # Handle database connection error
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    except Exception as e:
        # Handle general errors
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        # Close cursor and connection
        if conn.open:
            cursor.close()
            conn.close()

# Function to insert employee records from CSV into database
def create_emps():
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        
        # SQL query for inserting employee records
        query = """
        INSERT INTO ust_aims_plus.employee_directory(
            emp_code,full_name,email,phone,department,location,join_date,status
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        
        # Open employee CSV file
        with open("C:/Users/Administrator/Desktop/AIMS_update/database/sampledata/final_data/validated_employee_directory.csv", "r") as file:
            content = csv.DictReader(file)
            
            for row in content:
                try:
                    # Prepare employee data tuple
                    data = (
                        row["emp_code"], row["full_name"], row["email"], row["phone"],
                        row["department"], row["location"], row["join_date"], row["status"]
                    )
                    cursor.execute(query, data)
                except Exception as e:
                    # Handle invalid row data
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Invalid row data: {e}"
                    )
        conn.commit()
        return {"message": "Employee records inserted successfully"}
    except Exception as e:
        # Handle general database errors
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
# Function to insert maintenance records from CSV into database
def create_maintains():
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        
        # SQL query for inserting maintenance records
        query = """
        INSERT INTO ust_aims_plus.maintenance_log(
            asset_tag,maintenance_type,
            vendor_name,description,cost,
            maintenance_date,technician_name,status
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        
        # Open maintenance CSV file
        with open("C:/Users/Administrator/Desktop/AIMS_update/database/sampledata/final_data/validated_maintainence_log.csv", "r") as file:
            content = csv.DictReader(file)
            
            for row in content:
                try:
                    # Prepare maintenance data tuple
                    data = (
                        row["asset_tag"], row["maintenance_type"], row["vendor_name"],
                        row["description"], row["cost"], row["maintenance_date"],
                        row["technician_name"], row["status"]
                    )
                    cursor.execute(query, data)
                except Exception as e:
                    # Handle invalid row data
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Invalid row data: {e}"
                    )
        conn.commit()
        return {"message": "Maintenance records inserted successfully"}
    except Exception as e:
        # Handle general database errors
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# Function to insert vendor records from CSV into database
def create_vendors():
    try:
        conn = db_connection.get_Connection()
        cursor = conn.cursor()
        
        # SQL query for inserting vendor records
        query = """
        INSERT INTO ust_aims_plus.vendor_master(
             vendor_name,contact_person,contact_phone,gst_number,email,address,city,active_status
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        
        # Open vendor CSV file
        with open("C:/Users/Administrator/Desktop/AIMS_update/database/sampledata/final_data/validated_vendor_master.csv", "r") as file:
            content = csv.DictReader(file)
            
            for row in content:
                try:
                    # Prepare vendor data tuple
                    data = (
                        row["vendor_name"], row["contact_person"], row["contact_phone"],
                        row["gst_number"], row["email"], row["address"],
                        row["city"], row["active_status"]
                    )
                    cursor.execute(query, data)
                except Exception as e:
                    # Handle invalid row data
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Invalid row data: {e}"
                    )
        conn.commit()
        return {"message": "Vendor records inserted successfully"}
    except Exception as e:
        # Handle general database errors
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()
