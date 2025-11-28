USE ust_asset_db;

CREATE TABLE asset_inventory (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_tag VARCHAR(50),
    asset_type VARCHAR(50),
    serial_number VARCHAR(100),
    manufacturer VARCHAR(50),
    model VARCHAR(100),
    purchase_date DATE,
    warranty_years INT,
    condition_status VARCHAR(20),
    assigned_to VARCHAR(150),
    location VARCHAR(100),
    asset_status VARCHAR(20),
    last_updated DATETIME
);

CREATE TABLE vendor_master (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_name VARCHAR(100),
    contact_person VARCHAR(100),
    contact_phone VARCHAR(15),
    gst_number VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(200),
    city VARCHAR(100),
    active_status VARCHAR(10)
);
CREATE TABLE employee_master (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_code VARCHAR(20) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    department VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    join_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL
);
CREATE TABLE maintenance_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_tag VARCHAR(50),
    maintenance_type VARCHAR(20),
    vendor_name VARCHAR(100),
    description TEXT,
    cost DECIMAL(10,2),
    maintenance_date DATE,
    technician_name VARCHAR(100),
    status VARCHAR(20)
);
