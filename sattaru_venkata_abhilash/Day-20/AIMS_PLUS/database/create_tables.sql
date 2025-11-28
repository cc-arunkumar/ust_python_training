-- Create asset_inventory table
CREATE TABLE asset_inventory (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,  -- Auto incremented ID for each record
    asset_tag VARCHAR(50) NOT NULL,           -- Asset tag (e.g., UST-001, UST-MNT-1234)
    asset_type VARCHAR(50) NOT NULL,          -- Type of asset (Laptop, Monitor, etc.)
    serial_number VARCHAR(100) NOT NULL UNIQUE, -- Unique serial number for each asset
    manufacturer VARCHAR(50) NOT NULL,        -- Manufacturer (Dell, HP, etc.)
    model VARCHAR(100) NOT NULL,              -- Model number of the asset
    purchase_date DATE NOT NULL CHECK (purchase_date <= CURDATE()), -- Purchase date, cannot be future
    warranty_years INT NOT NULL CHECK (warranty_years BETWEEN 1 AND 5),  -- Warranty years (1-5)
    condition_status VARCHAR(20) NOT NULL CHECK (condition_status IN ('New', 'Good', 'Used', 'Damaged')),  -- Condition status
    assigned_to VARCHAR(150),                 -- Assigned to employee (Optional)
    location VARCHAR(100) NOT NULL,           -- Location (TVM/Bangalore/Chennai/Hyderabad)
    asset_status VARCHAR(20) NOT NULL CHECK (asset_status IN ('Available', 'Assigned', 'Repair', 'Retired')), -- Status of the asset
    last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Auto-updated on changes
);

-- Create employee_directory table
CREATE TABLE employee_directory (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,   -- Employee ID
    emp_code VARCHAR(20) NOT NULL,            -- Employee code (Must start with USTEMP)
    full_name VARCHAR(100) NOT NULL,          -- Full name (Alphabets + spaces)
    email VARCHAR(100) NOT NULL CHECK (email LIKE '%@ust.com'),  -- Email (Must end with @ust.com)
    phone VARCHAR(15) NOT NULL CHECK (phone REGEXP '^[0-9]{10}$'), -- Phone (10-digit Indian mobile number)
    department VARCHAR(50) NOT NULL CHECK (department IN ('HR', 'IT', 'Admin', 'Finance')),  -- Department
    location VARCHAR(100) NOT NULL,           -- Employee location (Indian UST locations)
    join_date DATE NOT NULL CHECK (join_date <= CURDATE()), -- Join date (Cannot be future)
    status VARCHAR(20) NOT NULL CHECK (status IN ('Active', 'Inactive', 'Resigned')) -- Employment status
);

-- Create vendor_master table
CREATE TABLE vendor_master (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY, -- Vendor ID
    vendor_name VARCHAR(100) NOT NULL CHECK (vendor_name NOT LIKE '%[0-9]%'), -- Vendor name (No digits)
    contact_person VARCHAR(100) NOT NULL CHECK (contact_person NOT LIKE '%[^a-zA-Z ]%'), -- Contact person's name (Alphabets only)
    contact_phone VARCHAR(15) NOT NULL CHECK (contact_phone REGEXP '^[0-9]{10}$'), -- Contact phone (Indian mobile number)
    gst_number VARCHAR(20) NOT NULL,         -- GST number (15 characters)
    email VARCHAR(100) NOT NULL CHECK (email LIKE '%@%'), -- Valid email
    address VARCHAR(200) NOT NULL,           -- Address
    city VARCHAR(100) NOT NULL,              -- City (Indian cities)
    active_status VARCHAR(20) NOT NULL CHECK (active_status IN ('Active', 'Inactive')) -- Vendor status
);

-- Create maintenance_log table
CREATE TABLE maintenance_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,     -- Log ID
    asset_tag VARCHAR(50) NOT NULL CHECK (asset_tag LIKE 'UST-%'), -- Asset tag (Must follow UST- pattern)
    maintenance_type VARCHAR(50) NOT NULL CHECK (maintenance_type IN ('Repair', 'Service', 'Upgrade')), -- Type of maintenance
    vendor_name VARCHAR(100) NOT NULL CHECK (vendor_name NOT LIKE '%[^a-zA-Z ]%'), -- Vendor name (Alphabets only)
    description VARCHAR(300) NOT NULL CHECK (CHAR_LENGTH(description) >= 10), -- Description (Minimum 10 characters)
    cost DECIMAL(10,2) NOT NULL CHECK (cost > 0), -- Maintenance cost (Must be greater than 0)
    maintenance_date DATE NOT NULL CHECK (maintenance_date <= CURDATE()), -- Maintenance date (Cannot be future)
    technician_name VARCHAR(100) NOT NULL CHECK (technician_name NOT LIKE '%[^a-zA-Z ]%'), -- Technician name (Alphabets only)
    status VARCHAR(20) NOT NULL CHECK (status IN ('Completed', 'Pending')) -- Maintenance status
);
