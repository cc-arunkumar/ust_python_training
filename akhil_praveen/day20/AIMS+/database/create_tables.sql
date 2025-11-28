.
-- Database schema for AIMS+ (ust_aims_plus)
-- This file creates tables used by the AIMS+ application:
--  - asset_inventory: stores asset records and status
--  - employee_directory: stores employee master data
--  - vendor_master: stores vendor details and contacts
--  - maintenance_log: records maintenance actions against assets
-- Notes:
--  - Use a dedicated database user with appropriate privileges.
--  - Ensure the database 'ust_aims_plus' exists before running these statements.
--  - Column types and constraints (UNIQUE, NOT NULL) enforce basic data integrity.

CREATE TABLE ust_aims_plus.asset_inventory (
    asset_id INT PRIMARY KEY AUTO_INCREMENT, -- surrogate primary key
    asset_tag VARCHAR(50) NOT NULL,           -- business identifier (human readable)
    asset_type VARCHAR(50) NOT NULL,          -- e.g. Laptop, Monitor
    serial_number VARCHAR(100) NOT NULL UNIQUE, -- unique hardware serial
    manufacturer VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    purchase_date DATE NOT NULL,               -- date of purchase
    warranty_years INT NOT NULL,               -- warranty period in years
    condition_status VARCHAR(20) NOT NULL,     -- e.g. Good, Faulty
    assigned_to VARCHAR(150),                  -- employee full_name or emp_code
    location VARCHAR(100) NOT NULL,            -- asset location / site
    asset_status VARCHAR(20) NOT NULL,         -- e.g. Assigned, Available, Retired
    last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- timestamp
);

-- Employee master table: unique constraints on email and phone to avoid duplicates.
CREATE TABLE ust_aims_plus.employee_directory (
    emp_id INT PRIMARY KEY AUTO_INCREMENT, -- surrogate primary key
    emp_code VARCHAR(20) NOT NULL,         -- employee code/id used in the org
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,    -- unique business email
    phone VARCHAR(15) NOT NULL UNIQUE,     -- unique contact number
    department VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    join_date DATE NOT NULL,               -- date employee joined
    status VARCHAR(20) NOT NULL            -- e.g. Active, Inactive
);

-- Vendor master table: store vendor contact and tax details.
CREATE TABLE ust_aims_plus.vendor_master (
    vendor_id INT PRIMARY KEY AUTO_INCREMENT, -- surrogate primary key
    vendor_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(15) NOT NULL,      -- phone number for vendor contact
    gst_number VARCHAR(20) NOT NULL,         -- GST / tax id
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(100) NOT NULL,
    active_status VARCHAR(20) NOT NULL       -- e.g. Active, Inactive
);

-- Maintenance log table: records maintenance events for assets.
CREATE TABLE ust_aims_plus.maintenance_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT, -- surrogate primary key
    asset_tag VARCHAR(50) NOT NULL,        -- references asset_inventory.asset_tag (no FK to keep lightweight)
    maintenance_type VARCHAR(50) NOT NULL, -- e.g. Repair, Service
    vendor_name VARCHAR(100) NOT NULL,     -- vendor involved in maintenance
    description VARCHAR(300) NOT NULL,     -- details of work done
    cost DECIMAL(10,2) NOT NULL,          -- cost of maintenance
    maintenance_date DATE NOT NULL,        -- when maintenance occurred
    technician_name VARCHAR(100) NOT NULL, -- who performed the maintenance
    status VARCHAR(20) NOT NULL            -- e.g. Completed, Pending
);
-- ...existing code...