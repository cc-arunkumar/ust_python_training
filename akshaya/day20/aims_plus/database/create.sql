-- Table to store information about asset inventory
CREATE TABLE aims_plus.asset_inventory (
    asset_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each asset, auto-incremented
    asset_tag VARCHAR(50) NOT NULL,  -- Unique asset tag for each asset, must not be null
    asset_type VARCHAR(50) NOT NULL,  -- Type of the asset (e.g., Laptop, Monitor), must not be null
    serial_number VARCHAR(100) NOT NULL UNIQUE,  -- Unique serial number for the asset, must not be null
    manufacturer VARCHAR(50) NOT NULL,  -- Manufacturer of the asset, must not be null
    model VARCHAR(100) NOT NULL,  -- Model of the asset, must not be null
    purchase_date DATE NOT NULL,  -- Date when the asset was purchased, must not be null
    warranty_years INT NOT NULL,  -- Number of years for warranty, must not be null
    condition_status VARCHAR(20) NOT NULL,  -- Condition of the asset (e.g., New, Used, Damaged), must not be null
    assigned_to VARCHAR(150),  -- Name of the person to whom the asset is assigned (optional)
    location VARCHAR(100) NOT NULL,  -- Location where the asset is stored, must not be null
    asset_status VARCHAR(20) NOT NULL,  -- Current status of the asset (e.g., Available, Assigned), must not be null
    last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the record was last updated, auto-updated on modification
);
 
-- Table to store employee directory information
CREATE TABLE aims_plus.employee_directory (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each employee, auto-incremented
    emp_code VARCHAR(20) NOT NULL,  -- Employee code, must not be null
    full_name VARCHAR(100) NOT NULL,  -- Full name of the employee, must not be null
    email VARCHAR(100) NOT NULL UNIQUE,  -- Email address of the employee, must be unique
    phone VARCHAR(15) NOT NULL UNIQUE,  -- Phone number of the employee, must be unique
    department VARCHAR(50) NOT NULL,  -- Department where the employee works, must not be null
    location VARCHAR(100) NOT NULL,  -- Location where the employee works, must not be null
    join_date DATE NOT NULL,  -- Date the employee joined the company, must not be null
    status VARCHAR(20) NOT NULL  -- Status of the employee (e.g., Active, Inactive), must not be null
);
 
-- Table to store vendor information
CREATE TABLE aims_plus.vendor_master (
    vendor_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each vendor, auto-incremented
    vendor_name VARCHAR(100) NOT NULL,  -- Name of the vendor, must not be null
    contact_person VARCHAR(100) NOT NULL,  -- Name of the contact person at the vendor, must not be null
    contact_phone VARCHAR(15) NOT NULL,  -- Contact phone number of the vendor, must not be null
    gst_number VARCHAR(20) NOT NULL,  -- GST number of the vendor, must not be null
    email VARCHAR(100) NOT NULL,  -- Email address of the vendor, must not be null
    address VARCHAR(200) NOT NULL,  -- Address of the vendor, must not be null
    city VARCHAR(100) NOT NULL,  -- City where the vendor is located, must not be null
    active_status VARCHAR(20) NOT NULL  -- Status of the vendor (e.g., Active, Inactive), must not be null
);
 
-- Table to store maintenance logs for assets
CREATE TABLE aims_plus.maintenance_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each maintenance log, auto-incremented
    asset_tag VARCHAR(50) NOT NULL,  -- Asset tag related to the maintenance log, must not be null
    maintenance_type VARCHAR(50) NOT NULL,  -- Type of maintenance (e.g., Repair, Service, Upgrade), must not be null
    vendor_name VARCHAR(100) NOT NULL,  -- Name of the vendor performing the maintenance, must not be null
    description VARCHAR(300) NOT NULL,  -- Description of the maintenance work performed, must not be null
    cost DECIMAL(10,2) NOT NULL,  -- Cost of the maintenance work, must not be null
    maintenance_date DATE NOT NULL,  -- Date the maintenance was performed, must not be null
    technician_name VARCHAR(100) NOT NULL,  -- Name of the technician who performed the maintenance, must not be null
    status VARCHAR(20) NOT NULL  -- Status of the maintenance (e.g., Completed, Pending), must not be null
);
