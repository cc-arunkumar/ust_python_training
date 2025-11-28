-- Create database if not exists
CREATE DATABASE IF NOT EXISTS ust_inventory_db;
USE ust_inventory_db;

-- 1. Employee Directory
CREATE TABLE employee_directory (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_code VARCHAR(20) NOT NULL ,
    full_name VARCHAR(100) NOT NULL ,
    email VARCHAR(100) NOT NULL ,
    phone VARCHAR(15) NOT NULL ,
    department VARCHAR(50) NOT NULL ,
    location VARCHAR(100) NOT NULL,
    join_date DATE NOT NULL ,
    status VARCHAR(20) NOT NULL 
);

-- 2. Vendor Master
CREATE TABLE vendor_master (
    vendor_id INT AUTO_INCREMENT PRIMARY KEY,
    vendor_name VARCHAR(100) NOT NULL ,
    contact_person VARCHAR(100) NOT NULL ,
    contact_phone VARCHAR(15) NOT NULL ,
    gst_number VARCHAR(20) NOT NULL ,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200),
    city VARCHAR(100) NOT NULL,
    active_status VARCHAR(20) NOT NULL 
);

-- 3. Maintenance Log
CREATE TABLE maintenance_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_tag VARCHAR(50) NOT NULL ,
    maintenance_type VARCHAR(50) NOT NULL ,
    vendor_name VARCHAR(100) NOT NULL ,
    description VARCHAR(300) NOT NULL ,
    cost DECIMAL(10,2) NOT NULL ,
    maintenance_date DATE NOT NULL ,
    technician_name VARCHAR(100) NOT NULL ,
    status VARCHAR(20) NOT NULL 
);

CREATE TABLE asset_inventory (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_tag VARCHAR(50) NOT NULL UNIQUE ,
    asset_type VARCHAR(50) NOT NULL CHECK ,
    serial_number VARCHAR(100) NOT NULL UNIQUE,
    manufacturer VARCHAR(50) NOT NULL ,
    model VARCHAR(100) NOT NULL,
    purchase_date DATE NOT NULL,
    warranty_years INT NOT NULL ,
    condition_status VARCHAR(20) NOT NULL ,
    assigned_to VARCHAR(150),
    location VARCHAR(100) NOT NULL ,
    asset_status VARCHAR(20) NOT NULL ,
    last_updated DATETIME NOT NULL 
);