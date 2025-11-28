from datetime import datetime
from src.config.db_connection import get_connection
import csv
def asset_model_connection():
    # print("going inside")
    current_time=datetime.now()
    conn=get_connection()
    cursor=conn.cursor()
    
    query="""
    INSERT INTO aims_db.assets_inventory
    (asset_tag, asset_type, serial_number, manufacturer, model,
    purchase_date, warranty_years, condition_status, assigned_to,
    location, asset_status,last_updated)
    VALUES 
    (
     %s,%s,%s,%s,%s,
     %s,%s,%s,%s,
     %s,%s,current_time
    )
    """
    updated_csv_file_assets=r'C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\output_data\valid_asset.csv'
    with open(updated_csv_file_assets,mode="r") as file:
        reader=csv.DictReader(file)
        
        for row in reader:
            data=(
                row["asset_tag"],
                row["asset_type"],
                row["serial_number"],
                row["manufacturer"],
                row["model"],
                row["purchase_date"],
                row["warranty_years"],
                row["condition_status"],
                row["assigned_to"],
                row["location"],
                row["asset_status"]
                )
            cursor.execute(query,data)
    conn.commit()
    cursor.close()
    conn.close()
    # print("All CSV recored dumped sucessfully")
        
        

def employee_model_connection():
    # Get the current timestamp for 'last_updated'
    # current_time = datetime.now()
    
    # Establish the database connection
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL query to insert data into the employee_directory table
    query = """
    INSERT INTO aims_db.employee_directory
    (emp_code, full_name, email, phone, department, location, join_date, status)
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s,%s)
    """
    
    # Path to the CSV file containing employee records
    updated_csv_file_employees = r'C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\output_data\valid_employee.csv'
    
    # Open the CSV file containing employee records
    with open(updated_csv_file_employees, mode="r") as file:
        reader = csv.DictReader(file)  # Read the CSV file as a dictionary
        
        for row in reader:
            # Prepare the data tuple for insertion
            data = (
                row["emp_code"],  
                row["full_name"], # Employee Code
                row["email"],         # Email
                row["phone"],         # Phone number
                row["department"],    # Department
                row["location"],      # Location
                row["join_date"],     # Join date
                row["status"],        # Status
                # current_time          # Setting the last_updated field to the current timestamp
            )
            
            # Execute the query for each row
            cursor.execute(query, data)
    conn.commit()
    
    # Commit the changes to the database
    
    
    # Close the cursor and the connection
    cursor.close()
    conn.close()
    
    # Output a success message
    # print("All CSV records dumped successfully into employee_directory table.")

# Call the function to insert records into the employee directory
# employee_model_connection()



def vendor_master_model_connection():
    # Get the current timestamp for 'last_updated'
    # current_time = datetime.now()
    
    # Establish the database connection
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL query to insert data into the employee_directory table
    query = """
    INSERT INTO aims_db.vendor_master
    (vendor_name, contact_person, contact_phone, gst_number, email, address, city, active_status)
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s,%s)
    """
    
    # Path to the CSV file containing employee records
    updated_csv_file_employees = r'C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\output_data\valid_vendor.csv'
    
    # Open the CSV file containing employee records
    with open(updated_csv_file_employees, mode="r") as file:
        reader = csv.DictReader(file)  # Read the CSV file as a dictionary
        
        for row in reader:
            # Prepare the data tuple for insertion
            data = (
                row["vendor_name"],  
                row["contact_person"], # Employee Code
                row["contact_phone"],         # Email
                row["gst_number"],         # Phone number
                row["email"],    # Department
                row["address"],      # Location
                row["city"],     # Join date
                row["active_status"],        # Status
                # current_time          # Setting the last_updated field to the current timestamp
            )
            
            # Execute the query for each row
            cursor.execute(query, data)
    conn.commit()
    
    # Commit the changes to the database
    
    
    # Close the cursor and the connection
    cursor.close()
    conn.close()
    
    # Output a success message
    # print("All CSV records dumped successfully into vendor_master table.")

# Call the function to insert records into the employee directory
# vendor_master_model_connection()

def maintenance_log_model_connection():
    # Get the current timestamp for 'last_updated'
    # current_time = datetime.now()
    
    # Establish the database connection
    conn = get_connection()
    cursor = conn.cursor()
    
    # SQL query to insert data into the employee_directory table
    query = """
    INSERT INTO aims_db.maintenance_log
    (asset_tag, maintenance_type, vendor_name, description, cost, maintenance_date, technician_name, status)
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s,%s)
    """
    
    # Path to the CSV file containing employee records
    updated_csv_file_employees = r'C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\output_data\valid_maintainence.csv'
    
    # Open the CSV file containing employee records
    with open(updated_csv_file_employees, mode="r") as file:
        reader = csv.DictReader(file)  # Read the CSV file as a dictionary
        
        for row in reader:
            # Prepare the data tuple for insertion
            data = (
                row["asset_tag"],  
                row["maintenance_type"], # Employee Code
                row["vendor_name"],         # Email
                row["description"],         # Phone number
                row["cost"],    # Department
                row["maintenance_date"],      # Location
                row["technician_name"],     # Join date
                row["status"],        # Status
                # current_time          # Setting the last_updated field to the current timestamp
            )
            
            # Execute the query for each row
            cursor.execute(query, data)
    conn.commit()
    
    # Commit the changes to the database
    
    
    # Close the cursor and the connection
    cursor.close()
    conn.close()
    
    # Output a success message
    # print("All CSV records dumped successfully into maintanence table.")

# Call the function to insert records into the employee directory
maintenance_log_model_connection()
