
CREATE TABLE IF NOT EXISTS asset_inventory (
  asset_id INT PRIMARY KEY AUTO_INCREMENT,
  asset_tag VARCHAR(50) NOT NULL,       
  asset_type VARCHAR(50) NOT NULL,      
  serial_number VARCHAR(100) NOT NULL,   
  manufacturer VARCHAR(50) NOT NULL,     
  model VARCHAR(100) NOT NULL,
  purchase_date DATE NOT NULL,
  warranty_years INT NOT NULL,
  condition_status VARCHAR(20) NOT NULL,
  assigned_to VARCHAR(150),
  location VARCHAR(100) NOT NULL,
  asset_status VARCHAR(20) NOT NULL,
  last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE (serial_number)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS employee_directory (
  emp_id INT PRIMARY KEY AUTO_INCREMENT,
  emp_code VARCHAR(20) NOT NULL,         
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  phone VARCHAR(15) NOT NULL,
  department VARCHAR(50) NOT NULL,
  location VARCHAR(100) NOT NULL,
  join_date DATE NOT NULL,
  status VARCHAR(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS vendor_master (
  vendor_id INT PRIMARY KEY AUTO_INCREMENT,
  vendor_name VARCHAR(100) NOT NULL,
  contact_person VARCHAR(100) NOT NULL,
  contact_phone VARCHAR(15) NOT NULL,
  gst_number VARCHAR(20) NOT NULL,     
  email VARCHAR(100) NOT NULL,
  address VARCHAR(200) NOT NULL,
  city VARCHAR(100) NOT NULL,
  active_status VARCHAR(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS maintenance_log (
  log_id INT PRIMARY KEY AUTO_INCREMENT,
  asset_tag VARCHAR(50) NOT NULL,         
  maintenance_type VARCHAR(50) NOT NULL,    
  vendor_name VARCHAR(100) NOT NULL,
  description VARCHAR(300) NOT NULL,
  cost DECIMAL(10,2) NOT NULL,
  maintenance_date DATE NOT NULL,
  technician_name VARCHAR(100) NOT NULL,
  status VARCHAR(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


