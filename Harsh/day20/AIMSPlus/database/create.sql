-- Switch to the database
USE ust_aims_db;

-- Table: Asset Inventory
CREATE TABLE asset_inventory (
    asset_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each asset
    asset_tag VARCHAR(50) NOT NULL,          -- Internal tag/label for asset tracking
    asset_type VARCHAR(50) NOT NULL,         -- Type/category of asset (e.g., Laptop, Printer)
    serial_number VARCHAR(100) NOT NULL UNIQUE, -- Manufacturer’s serial number, must be unique
    manufacturer VARCHAR(50) NOT NULL,       -- Asset manufacturer name
    model VARCHAR(100) NOT NULL,             -- Model name/number of the asset
    purchase_date DATE NOT NULL,             -- Date asset was purchased
    warranty_years INT NOT NULL,             -- Warranty period in years
    condition_status VARCHAR(20) NOT NULL,   -- Current condition (e.g., New, Used, Damaged)
    assigned_to VARCHAR(150),                -- Employee name or ID to whom asset is assigned
    location VARCHAR(100) NOT NULL,          -- Physical location of the asset
    asset_status VARCHAR(20) NOT NULL,       -- Status (e.g., Active, Retired, In Repair)
    last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP          -- Timestamp of last update
);

-- Table: Employee Directory
CREATE TABLE employee_directory (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each employee
    emp_code VARCHAR(20),                    -- Internal employee code
    full_name VARCHAR(100),                  -- Full name of employee
    email VARCHAR(100) UNIQUE,                     -- Employee email address
    phone VARCHAR(15) UNIQUE,                       -- Contact phone number
    department VARCHAR(50),                  -- Department name
    location VARCHAR(100),                   -- Work location/branch
    join_date DATE,                          -- Date employee joined the organization
    status VARCHAR(20)                       -- Employment status (e.g., Active, Resigned)
);

-- Table: Maintenance Log
CREATE TABLE maintenance_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each maintenance record
    asset_tag VARCHAR(50) NOT NULL,          -- Asset tag being serviced
    maintenance_type VARCHAR(50) NOT NULL,   -- Type of maintenance (e.g., Preventive, Repair)
    vendor_name VARCHAR(100) NOT NULL,       -- Vendor/company performing maintenance
    description VARCHAR(300) NOT NULL,       -- Description of maintenance work
    cost DECIMAL(10,2) NOT NULL,             -- Cost incurred for maintenance
    maintenance_date DATE NOT NULL,          -- Date maintenance was performed
    technician_name VARCHAR(100) NOT NULL,   -- Name of technician who performed the work
    status VARCHAR(20) NOT NULL              -- Status of maintenance (e.g., Completed, Pending)
);

-- Table: Vendor Master
CREATE TABLE vendor_master (
    vendor_id INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each vendor
    vendor_name VARCHAR(100) NOT NULL,        -- Vendor company name
    contact_person VARCHAR(100) NOT NULL,     -- Primary contact person at vendor
    contact_phone VARCHAR(15) NOT NULL,       -- Contact phone number
    gst_number VARCHAR(20) NOT NULL,          -- GST number for compliance
    email VARCHAR(100) NOT NULL,              -- Vendor email address
    address VARCHAR(200) NOT NULL,            -- Vendor address
    city VARCHAR(100) NOT NULL,               -- City where vendor is located
    active_status VARCHAR(20) NOT NULL        -- Vendor status (e.g., Active, Inactive)
);
