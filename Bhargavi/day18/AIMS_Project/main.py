# CRUD Task
# UST INTERNAL PROJECT REQUIREMENT
# DOCUMENT

# Project Title: Asset Inventory Management System
# (AIMS)
# Technology: Python + MySQL
# Document Version: 1.0
# Prepared For: UST Python Training Program
# Prepared By: Technical Trainer

# 1. PROJECT OVERVIEW
# UST manages thousands of hardware assets for employees in multiple locations
# (laptops, monitors, docking stations, etc.).
# The IT Asset Management (ITAM) team needs a backend system to:
# Store asset information
# Track asset assignments
# Update their condition/status
# Remove retired assets
# This project focuses on building the Asset Inventory module, which will allow
# internal IT teams to create, read, update, and delete asset records using Python +
# MySQL.
# CRUD Task 1

# 2. PROBLEM STATEMENT
# Currently UST’s IT team uses Excel sheets to track company assets.
# This causes:
# Duplicate records
# Loss of data
# Difficulty in searching
# No audit trail
# UST wants a proper database-backed system.
# As part of training, you must build the backend logic for database operations
# (CRUD).

# 3. SYSTEM SCOPE
# Python backend for CRUD operations
# MySQL database table and queries
# Validation logic
# NO UI
# NO API
# NO authentication
# NO business workflows
# Focus only on the Asset table.
# 4. DATABASE DETAILS (NO ASSUMPTIONS)
# Database Name: ust_asset_db
# (You MUST use this exact name.)
# CRUD Task 2
# Table Name: asset_inventory
# (You MUST use this exact name.)
# Table Structure (FINAL — no modifications allowed):
# Column Name Type Constraints Description
# asset_id INT
# PRIMARY KEY,
# AUTO_INCREMENT Unique asset identifier
# asset_tag VARCHAR(50) UNIQUE, NOT NULL
# Company asset tag (e.g., UST-LTP-000293)
# asset_type VARCHAR(50) NOT NULL
# Type of asset (Laptop, Monitor,
# Docking Station, Keyboard,
# Mouse)
# serial_number VARCHAR(100) UNIQUE, NOT NULL Manufacturer serial number
# manufacturer VARCHAR(50) NOT NULL Dell, HP, Lenovo etc.
# model VARCHAR(100) NOT NULL
# Asset model (e.g. “Latitude
# 5520”)
# purchase_date DATE NOT NULL Date when asset was purchased
# warranty_years INT NOT NULL, >0 Warranty validity in years
# assigned_to VARCHAR(100) NULL
# Employee name or NULL if
# unassigned
# asset_status VARCHAR(20) NOT NULL
# Must be: “Available”, “Assigned”,
# “Repair”, “Retired”
# last_updated DATETIME NOT NULL
# Every UPDATE must refresh this
# timestamp

# 5. BUSINESS RULES
# Asset status allowed values:
# Available
# Assigned
# CRUD Task 3
# Repair
# Retired
# asset_tag must always start with:
# UST Example: UST-LTP-00321
# Warranty must be greater than 0.
# assigned_to must be NULL if asset_status = "Available" or
# "Retired".
# assigned_to must NOT be NULL if asset_status = "Assigned".
# Every update must update last_updated to current timestamp.
# 6. PYTHON REQUIREMENTS
# You must build 5 functions, and each must:
# Contain extremely detailed comments
# Use parameterized SQL queries
# Validate inputs before performing operations
# Handle errors gracefully
# Close connection & cursor in finally block
# Use a single get_connection() function

# 7. CRUD TASKS
# Below are the tasks EXACTLY as the trainee must implement.
# CRUD Task 4
# TASK 1: CREATE ASSET RECORD
# Function Name:
# create_asset()
# Inputs:
# asset_tag
# asset_type
# serial_number
# manufacturer
# model
# purchase_date
# warranty_years
# assigned_to (optional)
# asset_status
# Validations (all mandatory):
# 1. asset_tag must start with "UST-"
# 2. asset_type must be one of:
# “Laptop”, “Monitor”, “Docking Station”, “Keyboard”, “Mouse”
# 3. warranty_years > 0
# 4. If asset_status = "Assigned" → assigned_to must NOT be null
# 5. If asset_status = "Available"/"Retired" → assigned_to MUST be null
# 6. serial_number must be unique
# 7. asset_tag must be unique
# 8. last_updated = NOW() automatically

# CRUD Task 5
# Output:
# Success message + asset_id
# Error if validation fails
# TASK 2: READ ALL ASSET RECORDS
# Function Name:
# read_all_assets()
# Requirements:
# Retrieve all assets ordered by asset_id ascending
# Option to pass filter:
# status_filter = “Available” / “Assigned” / “Repair” / “Retired” / “ALL”
# Default filter = “ALL”
# Output:
# Print all columns in readable format
# If no records found → print “No assets found.”
# TASK 3: READ ASSET BY ID
# Function Name:
# read_asset_by_id(asset_id)
# Requirements:
# If asset_id invalid → print “Asset not found.”
# CRUD Task 6
# Print complete asset details
# TASK 4: UPDATE EXISTING ASSET
# Function Name:
# update_asset(asset_id, …fields…)
# Fields that can be updated:
# asset_type
# manufacturer
# model
# warranty_years
# asset_status
# assigned_to
# VALIDATIONS:
# Same as in CREATE + asset_id must exist
# Additional Rules:
# last_updated MUST update to datetime.NOW()
# TASK 5: DELETE ASSET
# Function Name:
# delete_asset(asset_id)
# Requirements:
# This is a hard delete (record removed permanently)
# CRUD Task 7
# If asset_id does not exist → print “Asset not found.”
# 8. DELIVERABLES
# The trainee must submit:
# 1. asset_crud.py
# All CRUD functions
# get_connection()
# Deep comments explaining every line
# 2. aims_demo.py
# Script that calls every CRUD function at least once
# 3. SQL file:
# Contains table creation script
# 9. NON-FUNCTIONAL REQUIREMENTS
# Code must be readable
# Deep comments for every line
# No repeated code
# Proper exception handling
# No global variables
# Use docstrings
# Use snake_case naming
# 10. ER Diagram
# CRUD Task 8
# SAMPLE DATA
# 1. Available Assets (Not assigned to anyone)
# INSERT INTO asset_inventory
# (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, w
# arranty_years, assigned_to, asset_status, last_updated)
# VALUES
# ('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-01-15', 3, NULL, 'Available', NOW()),
# ('UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', '20
# 22-10-10', 2, NULL, 'Available', NOW()),
# ('UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', '2023-0
# 5-01', 1, NULL, 'Available', NOW());
# CRUD Task 9
# 2. Assigned Assets (Assigned to UST employees)
# INSERT INTO asset_inventory
# (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, w
# arranty_years, assigned_to, asset_status, last_updated)
# VALUES
# ('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', '2022-05-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', NOW()),
# ('UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', '20
# 21-11-20', 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', NOW()),
# ('UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R
# 350', '2023-03-12', 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned', NOW());
# 3. Assets in Repair
# INSERT INTO asset_inventory
# (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, w
# arranty_years, assigned_to, asset_status, last_updated)
# VALUES
# ('UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', '202
# 1-09-18', 3, NULL, 'Repair', NOW());
# 4. Retired Assets (Old / End-of-life)
# INSERT INTO asset_inventory
# (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, w
# arranty_years, assigned_to, asset_status, last_updated)
# VALUES
# ('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-08-12', 3, NULL, 'Retired', NOW());

import asset_crud

# Sample data to insert into the asset database
data = [
    ('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-01-15', 3, None, 'Available'),
    ('UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', '2022-10-10', 2, None, 'Available'),
    ('UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', '2023-05-01', 1, None, 'Available'),
    ('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', '2022-05-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned'),
    ('UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', '2021-11-20', 3, 'Anjali Nair (UST Trivandrum)', 'Assigned'),
    ('UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', '2023-03-12', 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned'),
    ('UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', '2021-09-18', 3, None, 'Repair'),
    ('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-08-12', 3, None, 'Retired')
]

# ----------------- Inserting Assets ----------------
# Inserting all assets in the `data` list into the database
print("\n************* Inserting Assets ***********")
for item in data:
    asset_crud.create_asset(item)  # Calls the `create_asset` function to insert each asset

# ----------------- Read All Assets ----------------
# Fetching and displaying all assets from the database (without any filters)
print("\n************* Read ALL assets ***********")
asset_crud.read_all_assets()  # Calls the `read_all_assets` function to get all asset records

# ----------------- Read Available Assets ----------------
# Fetching and displaying only the assets that are "Available"
print("\n************* Read Available assets ***********")
asset_crud.read_all_assets("Available")  # Filters the assets to display only those with status 'Available'

# ----------------- Read Asset by ID ----------------
# Fetching and displaying the asset with ID = 3
print("\n************* Read asset by ID = 3 ***********")
asset_crud.read_asset(3)  # Fetches the asset record with asset_id = 3

# ----------------- Update Asset ----------------
# Updating the details of the asset with ID = 3
print("\n************* Update Asset ID = 3 ***********")
updated_data = (
    'UST-LTP-0999', 'Laptop', 'SN-HP-NEW9911', 'HP', 'HP EliteBook 845',  # New asset details
    '2023-06-01', 2, None, 'Available'  # Warranty of 2 years, status 'Available'
)
asset_crud.update_asset(3, updated_data)  # Calls the `update_asset` function to update the asset with ID = 3

# ----------------- Delete Asset ----------------
# Deleting the asset with ID = 5 from the database
print("\n************* Delete Asset ID = 5 ***********")
asset_crud.delete_asset(5)  # Calls the `delete_asset` function to delete the asset with ID = 5

# ----------------- Final List of Assets ----------------
# Fetching and displaying the final list of assets after the update and deletion operations
print("\n************* Final List ***********")
asset_crud.read_all_assets()  # Fetches and displays all the remaining assets

#output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day18\AIMS_Project>
# ************* Inserting Assets ***********
# DB Connection Established  
# Asset inserted successfully
# DB Connection Established  
# Asset inserted successfully
# DB Connection Established  
# Asset inserted successfully
# DB Connection Established  
# Asset inserted successfully
# DB Connection Established  
# Asset inserted successfully
# DB Connection Established  
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully

# ************* Read ALL assets ***********
# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (2, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 
# 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (4, 'UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', datetime.date(2022, 5, 11), 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (5, 'UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', datetime.date(2021, 11, 20), 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (6, 'UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', datetime.date(2023, 3, 12), 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (7, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 27, 5, 25, 20))

# ************* Read Available assets ***********
# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (2, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 
# 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))

# ************* Read asset by ID = 3 ***********
# DB Connection Established
# Asset: (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))

# ************* Update Asset ID = 3 ***********
# DB Connection Established
# Asset: (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# DB Connection Established
# Asset updated successfully

# ************* Delete Asset ID = 5 ***********
# DB Connection Established
# Asset: (5, 'UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', datetime.date(2021, 11, 20), 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', datetime.datetime(2025, 11, 27, 5, 25, 20))
# DB Connection Established
# Asset deleted

# ************* Final List ***********
# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (2, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 
# 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (3, 'UST-LTP-0999', 'Laptop', 'SN-HP-NEW9911', 'HP', 'HP EliteBook 845', datetime.date(2023, 6, 1), 2, None, 'Available', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (4, 'UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', datetime.date(2022, 5, 11), 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (6, 'UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', datetime.date(2023, 3, 12), 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (7, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 27, 5, 25, 20))
# (8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 27, 5, 25, 20))
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day18\AIMS_Project>