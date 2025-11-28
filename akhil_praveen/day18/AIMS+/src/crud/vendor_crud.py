import pymysql
from typing import Optional
from ..models.vendormaster import VendorMaster, StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv

# Function to retrieve column names from the vendor_master table
def get_keys():
    try:
        conn = get_connection()  # Establish the database connection
        cursor = conn.cursor()
        
        # Query to fetch column names of the vendor_master table
        cursor.execute("""SELECT COLUMN_NAME
                          FROM INFORMATION_SCHEMA.COLUMNS
                          WHERE TABLE_SCHEMA = 'ust_aims_plus'
                          AND TABLE_NAME = 'vendor_master'
                          ORDER BY ORDINAL_POSITION;""")
        col = cursor.fetchall()
        keys = []
        
        # Add each column name to the keys list
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

# Class for performing CRUD operations on vendor data in the database
class VendorCrud:
    
    # Method to insert a new vendor record into the database
    def create_vendor(self, data: VendorMaster):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to insert a new vendor record
            query = """
            insert into ust_aims_plus.vendor_master (vendor_name, contact_person, contact_phone,
            gst_number, email, address, city, active_status) 
            values (%s, %s, %s, %s,
            %s, %s, %s, %s)
            """
            values = tuple(data.__dict__.values())  # Convert the data object to a tuple
            cursor.execute(query, values)  # Execute the insertion query
            conn.commit()  # Commit the transaction to save changes
            print("Data added successfully!")
            return data  # Return the newly created vendor data
            
        except Exception as e:
            print(e)
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to retrieve all vendor records or filter by status
    def get_all_vendor(self, status):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the vendor_master table
            keys = get_keys()
            
            # Query to retrieve vendor records based on the provided status
            if status == "ALL":
                query = """select * from ust_aims_plus.vendor_master"""
                cursor.execute(query)
            else:
                query = """select * from ust_aims_plus.vendor_master where status = %s"""
                cursor.execute(query, (status,))
            
            rows = cursor.fetchall()  # Fetch all rows from the query
            if rows:
                list_rows = []
                # Convert each row into a dictionary using column names as keys
                for values in rows:
                    list_rows.append(dict(zip(keys, values)))
                return list_rows  # Return the list of vendors
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

    # Method to retrieve a vendor record by its vendor ID
    def get_vendor_by_id(self, vendor_id):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the vendor_master table
            keys = get_keys()
            query = """select * from ust_aims_plus.vendor_master where vendor_id = %s"""
            cursor.execute(query, (vendor_id,))
            row = cursor.fetchone()  # Fetch a single row by vendor ID
            if row:
                list_rows = [dict(zip(keys, row))]  # Convert the row into a dictionary
                return list_rows  # Return the found vendor data
            else:
                raise  # Raise an exception if vendor is not found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to update an existing vendor record by vendor ID
    def update_vendor(self, id, data: VendorMaster):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to update the vendor data by vendor ID
            query = """
            update ust_aims_plus.vendor_master set vendor_name=%s, contact_person=%s, contact_phone=%s, gst_number=%s,
            email=%s, address=%s, city=%s, active_status=%s where vendor_id=%s
            """
            values = tuple(data.__dict__.values()) + (id,)  # Append the vendor ID to the values tuple
            cursor.execute(query, values)  # Execute the update query
            conn.commit()  # Commit the transaction to save the changes
            print("Data updated successfully!")
            return data  # Return the updated vendor data
            
        except Exception as e:
            print(str(e))
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to update the status of a vendor record by vendor ID
    def update_vendor_status(self, id, status):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to update the vendor status
            query = """update ust_aims_plus.vendor_master set status=%s where vendor_id=%s"""
            values = (status, id)  # Set the status and vendor ID
            cursor.execute(query, values)  # Execute the update query
            conn.commit()  # Commit the transaction to save the changes
            print("Status updated!")
            return self.get_vendor_by_id(id)  # Return the updated vendor data
                
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to delete a vendor record by vendor ID
    def delete_vendor(self, id):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            condition = self.get_vendor_by_id(id)  # Check if the vendor exists
            if condition:
                # Query to delete the vendor by vendor ID
                query = """delete from ust_aims_plus.vendor_master where vendor_id=%s"""
                values = (id,)  # Set the vendor ID to be deleted
                cursor.execute(query, values)  # Execute the delete query
                conn.commit()  # Commit the transaction to delete the vendor
                print("Vendor deleted from id =", id)
                keys = get_keys()
                list_rows = [dict(zip(keys, condition))]  # Convert the deleted vendor data to a dictionary
                return list_rows  # Return the deleted vendor data
                
            else:
                raise  # Raise exception if vendor is not found
                
        except Exception as e:
            print(e)
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to search for vendors by a specific keyword and value
    def get_vendor_by_keyword(self, keyword, value):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the vendor_master table
            keys = get_keys()
            
            # Construct the query to search for vendors by the given keyword
            query = f"""select * from ust_aims_plus.vendor_master where {keyword}=%s"""
            cursor.execute(query, (value,))
            rows = cursor.fetchall()  # Fetch all matching rows
            if rows:
                list_rows = []
                # Convert each row into a dictionary
                for values in rows:
                    list_rows.append(dict(zip(keys, values)))
                return list_rows  # Return the matched vendors
            else:
                raise  # Raise exception if no vendors are found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to get the total count of vendors in the vendor_master table
    def get_all_vendor_count(self):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            query = """select * from ust_aims_plus.vendor_master"""
            cursor.execute(query)
            rows = cursor.fetchall()  # Fetch all rows
            if rows:
                return len(rows)  # Return the count of rows (vendors)
            else:
                return None  # Return None if no vendors are found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    
    # Method to bulk upload assets from a CSV file  
    def bluk_upload(self):
        try:
            with open("path/to/vendor_master.csv","r") as vendor_file:
                csv_file = csv.DictReader(vendor_file)
                for data in csv_file:
                    self.create_vendor(data)
        except Exception as e:
            return e
