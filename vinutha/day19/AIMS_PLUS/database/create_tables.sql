--for creating Sql database
CREATE DATABASE ust_assets_db;


-- 1 asset_inventory table
CREATE TABLE asset_inventory (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_tag VARCHAR(50) NOT NULL,
    asset_type VARCHAR(50) NOT NULL,
    serial_number VARCHAR(100) NOT NULL UNIQUE,
    manufacturer VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    purchase_date DATE NOT NULL,
    warranty_years INT NOT NULL,
    condition_status VARCHAR(20) NOT NULL,
    assigned_to VARCHAR(150),
    location VARCHAR(100) NOT NULL,
    asset_status VARCHAR(20) NOT NULL,
    last_updated DATETIME NOT NULL
);

--2 employee_directory table

CREATE TABLE employee_directory (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_code VARCHAR(20) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    department VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    join_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL
);

-- 3 vendor_master table
CREATE TABLE vendor_master (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(15) NOT NULL,
    gst_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(100) NOT NULL,
    active_status VARCHAR(20) NOT NULL
);

--4 maintenance_log table

CREATE TABLE maintenance_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_tag VARCHAR(50) NOT NULL,
    maintenance_type VARCHAR(50) NOT NULL,
    vendor_name VARCHAR(100) NOT NULL,
    description VARCHAR(300) NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    maintenance_date DATE NOT NULL,
    technician_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL
);
