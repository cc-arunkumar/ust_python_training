CREATE TABLE ust_aims_plus.asset_inventory (
    asset_id INT PRIMARY KEY AUTO_INCREMENT,
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
    last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE ust_aims_plus.employee_directory (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_code VARCHAR(20) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL UNIQUE,
    department VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL,
    join_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE ust_aims_plus.vendor_master (
    vendor_id INT PRIMARY KEY AUTO_INCREMENT,
    vendor_name VARCHAR(100) NOT NULL,
    contact_person VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(15) NOT NULL,
    gst_number VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    city VARCHAR(100) NOT NULL,
    active_status VARCHAR(20) NOT NULL
);

CREATE TABLE ust_aims_plus.maintenance_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    asset_tag VARCHAR(50) NOT NULL,
    maintenance_type VARCHAR(50) NOT NULL,
    vendor_name VARCHAR(100) NOT NULL,
    description VARCHAR(300) NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    maintenance_date DATE NOT NULL,
    technician_name VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL
);