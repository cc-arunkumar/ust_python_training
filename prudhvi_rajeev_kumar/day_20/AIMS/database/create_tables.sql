-- Use the database named 'ust_asset_db'
USE ust_asset_db;

-- Table to store asset inventory details
CREATE TABLE asset_inventory (
    -- Unique identifier for each asset (auto-incremented)
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Unique asset tag to identify the asset
    asset_tag VARCHAR(50),
    
    -- Type of the asset (e.g., Laptop, Monitor, etc.)
    asset_type VARCHAR(50),
    
    -- Serial number of the asset (unique identifier from the manufacturer)
    serial_number VARCHAR(100),
    
    -- Manufacturer of the asset (e.g., Dell, HP, etc.)
    manufacturer VARCHAR(50),
    
    -- Model of the asset
    model VARCHAR(100),
    
    -- Date when the asset was purchased
    purchase_date DATE,
    
    -- Number of years the asset is under warranty
    warranty_years INT,
    
    -- Condition of the asset (e.g., New, Good, Damaged)
    condition_status VARCHAR(20),
    
    -- Employee or department to whom the asset is assigned
    assigned_to VARCHAR(150),
    
    -- Location where the asset is kept (e.g., Office, Warehouse)
    location VARCHAR(100),
    
    -- Current status of the asset (e.g., Active, Retired, In Repair)
    asset_status VARCHAR(20),
    
    -- Date and time of the last update made to the asset record
    last_updated DATETIME
);

-- Table to store vendor details
CREATE TABLE vendor_master (
    -- Unique identifier for each vendor (auto-incremented)
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Name of the vendor
    vendor_name VARCHAR(100),
    
    -- Contact person at the vendor company
    contact_person VARCHAR(100),
    
    -- Contact phone number of the vendor
    contact_phone VARCHAR(15),
    
    -- GST (Goods and Services Tax) number of the vendor
    gst_number VARCHAR(15),
    
    -- Email address of the vendor
    email VARCHAR(100),
    
    -- Physical address of the vendor
    address VARCHAR(200),
    
    -- City where the vendor is located
    city VARCHAR(100),
    
    -- Indicates whether the vendor is active or not
    active_status VARCHAR(10)
);

-- Table to store employee master data
CREATE TABLE employee_master (
    -- Unique identifier for each employee (auto-incremented)
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    
    -- Employee code (unique for each employee)
    emp_code VARCHAR(20) NOT NULL,
    
    -- Full name of the employee
    full_name VARCHAR(100) NOT NULL,
    
    -- Email address of the employee
    email VARCHAR(100) NOT NULL,
    
    -- Phone number of the employee
    phone VARCHAR(15) NOT NULL,
    
    -- Department to which the employee belongs
    department VARCHAR(50) NOT NULL,
    
    -- Location where the employee is based (e.g., office, department)
    location VARCHAR(100) NOT NULL,
    
    -- Date when the employee joined the company
    join_date DATE NOT NULL,
    
    -- Current status of the employee (e.g., Active, On Leave, Terminated)
    status VARCHAR(20) NOT NULL
);

-- Table to store maintenance logs for assets
CREATE TABLE maintenance_log (
    -- Unique identifier for each maintenance log (auto-incremented)
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Asset tag associated with the maintenance (links to asset_inventory)
    asset_tag VARCHAR(50),
    
    -- Type of maintenance performed (e.g., Preventive, Corrective)
    maintenance_type VARCHAR(20),
    
    -- Name of the vendor providing the maintenance service
    vendor_name VARCHAR(100),
    
    -- Description of the maintenance work performed
    description TEXT,
    
    -- Cost incurred for the maintenance service
    cost DECIMAL(10,2),
    
    -- Date when the maintenance was performed
    maintenance_date DATE,
    
    -- Name of the technician who performed the maintenance
    technician_name VARCHAR(100),
    
    -- Status of the maintenance (e.g., Completed, Pending)
    status VARCHAR(20)
);
