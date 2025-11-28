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
# Company asset tag (e.g., USTLTP-000293)
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
# USTExample: UST-LTP-00321
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
# ('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-0115', 3, NULL, 'Available', NOW()),
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
# ('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', '202205-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', NOW()),
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
# ('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-0812', 3, NULL, 'Retired', NOW());
# CRUD Task 10
# Final Sample Dataset Summary
# asset_tag asset_type assigned_to asset_status
# UST-LTP-0001 Laptop NULL Available
# UST-MNT-0002 Monitor NULL Available
# UST-KEY-0003 Keyboard NULL Available
# UST-LTP-0004 Laptop Rohit Sharma (UST Bangalore) Assigned
# UST-DCK-0005 Docking Station Anjali Nair (UST Trivandrum) Assigned
# UST-MNT-0006 Monitor Vivek Reddy (UST Hyderabad) Assigned
# UST-LTP-0007 Laptop NULL Repair
# UST-MNT-0008 Monitor NULL Retired
# Perfect for CRUD testing.
# RECOMMENDED FOLDER STRUCTURE
# This is a real UST backend project folder structure (backend-only, no UI):
# AIMS_Project/
# │
# ├── database/
# │ ├── create_tables.sql # Contains table structure
# │ ├── sample_data.sql # Contains the sample inserts
# │
# ├── src/
# │ ├── config/
# │ │ └── db_connection.py # get_connection() function
# │ │
# │ ├── crud/
# │ │ └── asset_crud.py # All CRUD functions (deep comments)
# │ │
# │ ├── models/
# │ │ └── asset_model.py # Optional: asset class (if needed)
# │ │
# CRUD Task 11
# │ ├── helpers/
# │ │ └── validators.py # Input validation functions
# │ │
# │ └── main.py # Demo script calling CRUD operations
# │
# ├── logs/
# │ └── app.log # Future logging if added
# │
# └── README.md # Project description
# This structure is used in real UST backend projects → clean, modular, scalable.
# CRUD Task 12


        
from asset_crud import create_asset
from asset_crud import read_all_assets
from asset_crud import read_asset_by_id
from asset_crud import update_asset
from asset_crud import delete_asset
from datetime import datetime,date
create_asset(
    asset_tag="UST-LTP-0008",
    asset_type="Laptop",
    serial_number="SN-LN-9988123",
    manufacturer="Lenovo",
    model="ThinkPad T14",
    purchase_date=date(2022, 5, 10),
    warranty_years=3,
    assigned_to=None,              
    asset_status="Available",
    last_updated=datetime.now()
)
create_asset(
    asset_tag="UST-MNT-0009",
    asset_type="Monitor",
    serial_number="SN-SAM-7719231",
    manufacturer="Samsung",
    model="Samsung S24R350",
    purchase_date=date(2023, 3, 15),
    warranty_years=2,
    asset_status="Assigned",
    assigned_to="Priya Sharma (UST Pune)"
)
 
# Read and print all assets
read_all_assets()
 
 
# Fetch and print specific assets by id
read_asset_by_id(10)
read_asset_by_id(2)
 
 
# Update an asset (example)
update_asset(
    asset_type="Laptop",
    manufacturer="HP",
    model="HP ProBook 440 G8",
    warranty_years=3,
    asset_status="Available",
    assigned_to="Vivek Reddy (UST Hyderabad)",
    asset_id=10
)

 
# Delete example assets
delete_asset(9)
delete_asset(2)
 


#sample execution
#  ID: 17 | UST-LTP-0004 | UST-LTP-0004 | Monitor | SN-LN-1234987 | LG | UltraWide 29WL500 | 2022-05-11 | 2 | Available | Retired
# (17, 'UST-LTP-0004', 'Monitor', 'SN-LN-1234987', 'LG', 'UltraWide 29WL500', datetime.date(2022, 5, 11), 2, 'Available', 'Retired', datetime.datetime(2025, 11, 26, 17, 20, 41))