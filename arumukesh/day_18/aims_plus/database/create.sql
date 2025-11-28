# -------------------------------------------------------------
# DATABASE SCHEMA: UST AIMS PLUS
# This file defines all table structures used in the system.
# Comments begin with # and are NOT actual data rows.
# -------------------------------------------------------------

# ==============================
# TABLE: asset_inventory
# ==============================

TABLE_NAME,COLUMN_NAME,DATA_TYPE,CONSTRAINTS,DESCRIPTION
asset_inventory,asset_id,INT,PRIMARY KEY AUTO_INCREMENT,Unique asset record ID
asset_inventory,asset_tag,VARCHAR(50),NOT NULL,Unique equipment asset tag
asset_inventory,asset_type,VARCHAR(50),NOT NULL,Type of asset (Laptop/Server/Printer etc.)
asset_inventory,serial_number,VARCHAR(100),NOT NULL UNIQUE,Hardware serial number
asset_inventory,manufacturer,VARCHAR(50),NOT NULL,Brand of asset
asset_inventory,model,VARCHAR(100),NOT NULL,Model name/number
asset_inventory,purchase_date,DATE,NOT NULL,Purchase date of the asset
asset_inventory,warranty_years,INT,NOT NULL,Warranty validity in years
asset_inventory,condition_status,VARCHAR(20),NOT NULL,Good/Repair/Damaged
asset_inventory,assigned_to,VARCHAR(150),NULL,Employee name assigned (optional)
asset_inventory,location,VARCHAR(100),NOT NULL,Physical storage/usage location
asset_inventory,asset_status,VARCHAR(20),NOT NULL,Active/Inactive/Retired
asset_inventory,last_updated,DATETIME,DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,Last modification timestamp


# ==============================
# TABLE: employee_directory
# ==============================

TABLE_NAME,COLUMN_NAME,DATA_TYPE,CONSTRAINTS,DESCRIPTION
employee_directory,emp_id,INT,PRIMARY KEY AUTO_INCREMENT,Unique employee record ID
employee_directory,emp_code,VARCHAR(20),NOT NULL,Employee official code
employee_directory,full_name,VARCHAR(100),NOT NULL,Full employee name
employee_directory,email,VARCHAR(100),NOT NULL UNIQUE,Work email ID
employee_directory,phone,VARCHAR(15),NOT NULL UNIQUE,Contact number
employee_directory,department,VARCHAR(50),NOT NULL,Department assigned
employee_directory,location,VARCHAR(100),NOT NULL,Work location
employee_directory,join_date,DATE,NOT NULL,Employee joining date
employee_directory,status,VARCHAR(20),NOT NULL,Active/Inactive/Terminated


# ==============================
# TABLE: vendor_master
# ==============================

TABLE_NAME,COLUMN_NAME,DATA_TYPE,CONSTRAINTS,DESCRIPTION
vendor_master,vendor_id,INT,PRIMARY KEY AUTO_INCREMENT,Unique vendor ID
vendor_master,vendor_name,VARCHAR(100),NOT NULL,Vendor company name
vendor_master,contact_person,VARCHAR(100),NOT NULL,Vendor contact person name
vendor_master,contact_phone,VARCHAR(15),NOT NULL,Vendor phone number
vendor_master,gst_number,VARCHAR(20),NOT NULL,GST or tax registration ID
vendor_master,email,VARCHAR(100),NOT NULL,Vendor contact email
vendor_master,address,VARCHAR(200),NOT NULL,Full vendor address
vendor_master,city,VARCHAR(100),NOT NULL,Vendor city
vendor_master,active_status,VARCHAR(20),NOT NULL,Status: Active/Inactive


# ==============================
# TABLE: maintenance_log
# ==============================

TABLE_NAME,COLUMN_NAME,DATA_TYPE,CONSTRAINTS,DESCRIPTION
maintenance_log,log_id,INT,PRIMARY KEY AUTO_INCREMENT,Unique maintenance log ID
maintenance_log,asset_tag,VARCHAR(50),NOT NULL,Asset reference tag
maintenance_log,maintenance_type,VARCHAR(50),NOT NULL,Type: Repair/Upgrade/Service
maintenance_log,vendor_name,VARCHAR(100),NOT NULL,Vendor responsible for service
maintenance_log,description,VARCHAR(300),NOT NULL,Work description
maintenance_log,cost,DECIMAL(10,2),NOT NULL,Service or repair cost
maintenance_log,maintenance_date,DATE,NOT NULL,Date of maintenance
maintenance_log,technician_name,VARCHAR(100),NOT NULL,Technician name who performed service
maintenance_log,status,VARCHAR(20),NOT NULL,Pending/Completed/Cancelled
