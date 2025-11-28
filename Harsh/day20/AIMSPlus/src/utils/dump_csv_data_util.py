import pymysql
import csv

# Establish database connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_aims_db"
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# SQL query to insert records into asset_inventory table
query = """
INSERT INTO asset_inventory (
    asset_tag, asset_type, serial_number, manufacturer, model,
    purchase_date, warranty_years, condition_status, assigned_to,
    location, asset_status
) VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s,
    %s, %s
)
"""

# Open the validated CSV file for reading
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\final_data\validated_asset_inventory.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    # Iterate through each row in the CSV
    for row in reader:
        # Prepare data tuple for insertion
        data = (
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
        # Execute insert query with row data
        try:
            cursor.execute(query, data)
        except pymysql.err.IntegrityError as e:
            print(f"Skipping duplicate record: {row['serial_number']} ({e})")
        except Exception as e:
            print(f"Error inserting row {row}: {e}")
# Commit all changes to the database
conn.commit()


# #SQL query to insert records into employee_directory table
# query = """
# INSERT INTO employee_directory (
#     emp_code,full_name,email,
#     phone,department,location,join_date,status
# ) VALUES (
#     %s, %s, %s, %s, %s,
#     %s, %s, %s
# )
# """

# # Open the validated employee CSV file
# with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\final_data\validated_employee_directory.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     # Iterate through each row in the CSV
#     for row in reader:
#         # Prepare data tuple for insertion
#         data = (
#             row["emp_code"],
#             row["full_name"],
#             row["email"],
#             row["phone"],
#             row["department"],
#             row["location"],
#             row["join_date"],
#             row["status"],
#         )
#         # Execute insert query with row data
#         cursor.execute(query, data)

# # Commit all changes to the database
# conn.commit()

# #SQL query to insert records into maintenance_log table
# query = """
# INSERT INTO maintenance_log (
#     asset_tag,maintenance_type,vendor_name,
#     description,cost,maintenance_date,technician_name,status
# ) VALUES (
#     %s, %s, %s, %s, %s,
#     %s, %s, %s
# )
# """

# # Open the validated maintenance CSV file
# with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\final_data\validated_maintenance_valid.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     # Iterate through each row in the CSV
#     for row in reader:
#         # Prepare data tuple for insertion
#         data = (
#             row["asset_tag"],
#             row["maintenance_type"],
#             row["vendor_name"],
#             row["description"],
#             row["cost"],
#             row["maintenance_date"],
#             row["technician_name"],
#             row["status"],
#         )
#         # Execute insert query with row data
#         cursor.execute(query, data)
        
        

# # Commit all changes to the database
# conn.commit()

# query = """
# INSERT INTO vendor_master (
#     vendor_name,contact_person,contact_phone,
#     gst_number,email,address,city,active_status
# ) VALUES (
#     %s, %s, %s, %s, %s,
#     %s, %s, %s
# )
# """

# # Open the validated vendor CSV file
# with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\final_data\validated_vendor_master.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     # Iterate through each row in the CSV
#     for row in reader:
#         # Prepare data tuple for insertion
#         data = (
#             row["vendor_name"],
#             row["contact_person"],
#             row["contact_phone"],
#             row["gst_number"],
#             row["email"],
#             row["address"],
#             row["city"],
#             row["active_status"],
#         )
#         # Execute insert query with row data
#         cursor.execute(query, data)

# # Commit all changes to the database
# conn.commit()


# Close cursor and connection
cursor.close()
conn.close()




# Print success message
print("All CSV records inserted successfully!")


