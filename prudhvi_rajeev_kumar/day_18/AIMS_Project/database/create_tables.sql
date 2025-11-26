DROP DATABASE IF EXISTS ust_asset_db;
CREATE DATABASE ust_asset_db;
USE ust_asset_db;

CREATE TABLE asset_inventory (
  asset_id INT AUTO_INCREMENT PRIMARY KEY,
  asset_tag VARCHAR(50) NOT NULL UNIQUE,
  asset_type VARCHAR(50) NOT NULL,
  serial_number VARCHAR(100) NOT NULL UNIQUE,
  manufacturer VARCHAR(50) NOT NULL,
  model VARCHAR(100) NOT NULL,
  purchase_date DATE NOT NULL,
  warranty_years INT NOT NULL,
  assigned_to VARCHAR(100),
  asset_status VARCHAR(20) NOT NULL,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
