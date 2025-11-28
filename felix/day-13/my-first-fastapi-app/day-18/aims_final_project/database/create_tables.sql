-- =========================================================
-- Database: ust_aims_plus
-- Contains tables for assets, employees, vendors, and maintenance logs
-- =========================================================

-- ===========================
-- Table: asset_inventory
-- Stores details of all company assets
-- ===========================
CREATE TABLE ust_aims_plus.asset_inventory (
    asset_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each asset
    asset_tag VARCHAR(50) NOT NULL,            -- Internal asset tag/label
    asset_type VARCHAR(50) NOT NULL,           -- Type/category of asset (e.g., Laptop, Printer)
    serial_number VARCHAR(100) NOT NULL UNIQUE,-- Manufacturer serial number (must be unique)
    manufacturer VARCHAR(50) NOT NULL,         -- Asset manufacturer name
    model VARCHAR(100) NOT NULL,               -- Model name/number
    purchase_date DATE NOT NULL,               -- Date of purchase
    warranty_years INT NOT NULL,               -- Warranty period in years
    condition_status VARCHAR(20) NOT NULL,     -- Current condition (e.g., New, Used, Damaged)
    assigned_to VARCHAR(150),                  -- Employee assigned to asset (nullable)
    location VARCHAR(100) NOT NULL,            -- Physical location of asset
    asset_status VARCHAR(20) NOT NULL,         -- Status (e.g., Active, Retired, In Repair)
    last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP 
        ON UPDATE CURRENT_TIMESTAMP            -- Auto-updated timestamp for last modification
);

-- ===========================
-- Table: employee_directory
-- Stores employee details for asset assignment and tracking
-- ===========================
CREATE TABLE ust_aims_plus.employee_directory (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique employee ID
    emp_code VARCHAR(20) NOT NULL,             -- Internal employee code
    full_name VARCHAR(100) NOT NULL,           -- Full name of employee
    email VARCHAR(100) NOT NULL UNIQUE,        -- Employee email (must be unique)
    phone VARCHAR(15) NOT NULL UNIQUE,         -- Employee phone number (must be unique)
    department VARCHAR(50) NOT NULL,           -- Department name
    location VARCHAR(100) NOT NULL,            -- Work location
    join_date DATE NOT NULL,                   -- Date of joining
    status VARCHAR(20) NOT NULL                -- Employment status (e.g., Active, Resigned)
);

-- ===========================
-- Table: vendor_master
-- Stores vendor details for asset procurement and maintenance
-- ===========================
CREATE TABLE ust_aims_plus.vendor_master (
    vendor_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique vendor ID
    vendor_name VARCHAR(100) NOT NULL,         -- Vendor company name
    contact_person VARCHAR(100) NOT NULL,      -- Primary contact person
    contact_phone VARCHAR(15) NOT NULL,        -- Contact phone number
    gst_number VARCHAR(20) NOT NULL,           -- GST number for tax compliance
    email VARCHAR(100) NOT NULL,               -- Vendor email
    address VARCHAR(200) NOT NULL,             -- Vendor address
    city VARCHAR(100) NOT NULL,                -- City of vendor
    active_status VARCHAR(20) NOT NULL         -- Status (e.g., Active, Inactive)
);

-- ===========================
-- Table: maintenance_log
-- Tracks maintenance activities performed on assets
-- ===========================
CREATE TABLE ust_aims_plus.maintenance_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique log entry ID
    asset_tag VARCHAR(50) NOT NULL,            -- Asset tag being serviced
    maintenance_type VARCHAR(50) NOT NULL,     -- Type of maintenance (e.g., Repair, Upgrade)
    vendor_name VARCHAR(100) NOT NULL,         -- Vendor who performed maintenance
    description VARCHAR(300) NOT NULL,         -- Description of work done
    cost DECIMAL(10,2) NOT NULL,               -- Maintenance cost
    maintenance_date DATE NOT NULL,            -- Date of maintenance
    technician_name VARCHAR(100) NOT NULL,     -- Technician performing the work
    status VARCHAR(20) NOT NULL                -- Status (e.g., Completed, Pending)
);