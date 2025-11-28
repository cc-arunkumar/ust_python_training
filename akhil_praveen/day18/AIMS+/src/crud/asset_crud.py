import pymysql
from typing import Optional
from ..models.assets_model import AssetInventory, StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
from ..exception.custom_exceptions import InvalidInputException,DatabaseConnectionException,DuplicateRecordException,RecordNotFoundExcpetion,ValidationErrorException
import csv

# Function to retrieve column names (keys) from the asset_inventory table
def get_keys():
    try:
        conn = get_connection()  # Get database connection
        cursor = conn.cursor()
        
        # SQL query to get column names from the asset_inventory table
        cursor.execute("""SELECT COLUMN_NAME
                          FROM INFORMATION_SCHEMA.COLUMNS
                          WHERE TABLE_SCHEMA = 'ust_aims_plus'
                          AND TABLE_NAME = 'asset_inventory'
                          ORDER BY ORDINAL_POSITION;""")
        col = cursor.fetchall()
        keys = []
        
        # Extract column names (keys) from the query result
        for i in col:
            keys.append(i[0])
        return keys
    except Exception as e:
        raise 
    finally:
        # Ensure the connection is closed after use
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed!")

# Class for performing CRUD operations on the AssetInventory table
class AssetCrud:
    
    # Method to create a new asset in the database
    def create_asset(self, data: AssetInventory):
        try:
            conn = get_connection()  # Get database connection
            cursor = conn.cursor()
            
            # SQL query to insert asset data into the database
            query = """
            insert into ust_aims_plus.asset_inventory (asset_tag, asset_type, serial_number, manufacturer,
            model, purchase_date, warranty_years, condition_status,
            assigned_to, location, asset_status, last_updated) 
            values (%s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s)
            """
            # Create values tuple from the data object and append current datetime for last_updated
            values = tuple(data.__dict__.values()) + (datetime.now(),)
            cursor.execute(query, values)
            conn.commit()  # Commit the transaction to save data
            print("Data added successfully!")
            return data  # Return the created asset data
            
        except Exception as e:
            print(e)
            raise
        finally:
            # Ensure the connection is closed after use
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to retrieve all assets from the database
    def get_all_asset(self, status):
        try:
            conn = get_connection()  # Get database connection
            cursor = conn.cursor()
            
            # Retrieve column names (keys) for asset_inventory table
            keys = get_keys()
            
            # SQL query to retrieve all assets or filter by asset status
            if status == "ALL":
                query = """select * from ust_aims_plus.asset_inventory"""
                cursor.execute(query)
            else:
                query = """select * from ust_aims_plus.asset_inventory where asset_status = %s"""
                cursor.execute(query, (status,))
            
            rows = cursor.fetchall()
            if rows:
                list_rows = []
                # Convert the result rows into a list of dictionaries
                for values in rows:
                    list_rows.append(dict(zip(keys, values)))
                return list_rows  # Return the list of assets
            else:
                return None  # Return None if no assets are found
        except Exception as e:
            raise
        finally:
            # Ensure the connection is closed after use
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to retrieve an asset by its asset_id
    def get_asset_by_id(self, asset_id):
        try:
            conn = get_connection()  # Get database connection
            cursor = conn.cursor()
            
            # Retrieve column names (keys) for asset_inventory table
            keys = get_keys()
            query = """select * from ust_aims_plus.asset_inventory where asset_id = %s"""
            cursor.execute(query, (asset_id,))
            row = cursor.fetchone()
            if row:
                list_rows = [dict(zip(keys, row))]
                return list_rows  # Return the found asset
            else:
                raise  # Raise exception if asset is not found
        except Exception as e:
            raise
        finally:
            # Ensure the connection is closed after use
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to update an existing asset
    def update_asset(self, id, data: AssetInventory):
        try:
            conn = get_connection()  # Get database connection
            cursor = conn.cursor()
            
            # SQL query to update asset data
            query = """
            update ust_aims_plus.asset_inventory set asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s,
            model=%s, purchase_date=%s, warranty_years=%s, condition_status=%s,
            assigned_to=%s, location=%s, asset_status=%s, last_updated=%s 
            where asset_id=%s
            """
            values = tuple(data.__dict__.values()) + (datetime.now(), id)  # Append the asset_id for the WHERE clause
            cursor.execute(query, values)
            conn.commit()  # Commit the transaction to save changes
            print("Data updated successfully!")
            return data  # Return the updated asset data
            
        except Exception as e:
            print(str(e))
            raise
        finally:
            # Ensure the connection is closed after use
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to update the status of an asset
    def update_asset_status(self, id, status):
        try:
            conn = get_connection()  # Get database connection
            cursor = conn.cursor()
            query = """update ust_aims_plus.asset_inventory set asset_status=%s where asset_id=%s"""
            values = (status, id)
            cursor.execute(query, values)
            conn.commit()  # Commit the transaction to save status change
            print("Status updated!")
            return self.get_asset_by_id(id)  # Return the updated asset data
                
        except Exception as e:
            raise
        finally:
            # Ensure the connection is closed after use
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to delete an asset by its asset_id
    def delete_asset(self, id):
        try:
            conn = get_connection()  # Get database connection
            cursor = conn.cursor()
            condition = self.get_asset_by_id(id)  # Retrieve asset to be deleted
            if condition:
                query = """delete from ust_aims_plus.asset_inventory where asset_id=%s"""
                values = (id,)
                cursor.execute(query, values)
                conn.commit()  # Commit the transaction to delete the asset
                print("Asset deleted from id =", id)
                keys = get_keys()
                list_rows = [dict(zip(keys, condition))]
                return list_rows  # Return the deleted asset data
                
            else:
                raise  # Raise exception if asset is not found
                
        except Exception as e:
            print(e)
            raise
        finally:
            # Ensure the connection is closed after use
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to search for assets based on a specific keyword and value
    def get_asset_by_keyword(self, keyword, value):
        try:
            conn = get_connection()  # Get database connection
            cursor = conn.cursor()
            
            # Retrieve column names (keys) for asset_inventory table
            keys = get_keys()
            query = f"""select * from ust_aims_plus.asset_inventory where {keyword}=%s"""
            cursor.execute(query, (value,))
            rows = cursor.fetchall()
            if rows:
                list_rows = []
                # Convert the result rows into a list of dictionaries
                for values in rows:
                    list_rows.append(dict(zip(keys, values)))
                return list_rows  # Return the matched assets
            else:
                raise  # Raise exception if no assets are found
        except Exception as e:
            raise
        finally:
            # Ensure the connection is closed after use
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to get the total count of all assets in the database
    def get_all_asset_count(self):
        try:
            conn = get_connection()  # Get database connection
            cursor = conn.cursor()
            query = """select * from ust_aims_plus.asset_inventory"""
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return len(rows)  # Return the total count of assets
            else:
                return None  # Return None if no assets are found
        except Exception as e:
            raise
        finally:
            # Ensure the connection is closed after use
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to bulk upload assets from a CSV file
    def bluk_upload(self):
        try:
            # Open the CSV file containing asset data
            with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/asset_inventory.csv", "r") as asset_file:
                csv_file = csv.DictReader(asset_file)
                
                # Iterate over each row in the CSV file and insert it into the database
                for data in csv_file:
                    self.create_asset(data)
        except Exception as e:
            return e  # Return any error
