CREATE TABLE `asset_inventory` (
  `asset_id` int NOT NULL AUTO_INCREMENT,  -- Unique identifier for each asset
  `asset_tag` varchar(50) NOT NULL,  -- Tag used to uniquely identify the asset (e.g., 'UST-LTP-1234')
  `asset_type` varchar(50) NOT NULL,  -- Type of the asset (e.g., Laptop, Monitor)
  `serial_number` varchar(100) NOT NULL,  -- Unique serial number of the asset
  `manufacturer` varchar(50) NOT NULL,  -- Manufacturer of the asset
  `model` varchar(100) NOT NULL,  -- Model of the asset
  `purchase_date` date NOT NULL,  -- Date when the asset was purchased
  `warranty_years` int NOT NULL,  -- Warranty period in years
  `condition_status` varchar(20) NOT NULL,  -- Condition of the asset (e.g., New, Used, Broken)
  `assigned_to` varchar(150) DEFAULT NULL,  -- Employee or department the asset is assigned to (nullable)
  `location` varchar(100) NOT NULL,  -- Location of the asset (e.g., office, warehouse)
  `asset_status` varchar(20) NOT NULL,  -- Status of the asset (e.g., Active, Inactive)
  `last_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update to the asset record
  PRIMARY KEY (`asset_id`),  -- Primary key for the table
  UNIQUE KEY `serial_number` (`serial_number`)  -- Ensure that serial numbers are unique across the assets
) 




CREATE TABLE `employee_directory` (
  `emp_id` int NOT NULL AUTO_INCREMENT,  -- Unique employee identifier
  `emp_code` varchar(20) NOT NULL,  -- Employee code, e.g., employee ID or badge number
  `full_name` varchar(100) NOT NULL,  -- Full name of the employee
  `email` varchar(100) NOT NULL,  -- Employee email address
  `phone` varchar(15) NOT NULL,  -- Employee phone number
  `department` varchar(50) NOT NULL,  -- Department the employee belongs to
  `location` varchar(100) NOT NULL,  -- Location of the employee (e.g., office branch)
  `join_date` date NOT NULL,  -- Date the employee joined the company
  `status` varchar(20) NOT NULL,  -- Employment status (e.g., Active, Terminated)
  PRIMARY KEY (`emp_id`)  -- Primary key for the employee table
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `maintenance_log` (
  `log_id` int NOT NULL AUTO_INCREMENT,  -- Unique log entry identifier
  `asset_tag` varchar(50) NOT NULL,  -- Asset tag associated with the maintenance record
  `maintenance_type` varchar(50) NOT NULL,  -- Type of maintenance performed (e.g., Repair, Preventive)
  `vendor_name` varchar(100) NOT NULL,  -- Name of the vendor who performed the maintenance
  `description` varchar(300) NOT NULL,  -- Description of the maintenance task
  `cost` decimal(10,2) NOT NULL,  -- Cost of the maintenance performed
  `maintenance_date` date NOT NULL,  -- Date the maintenance was performed
  `technician_name` varchar(100) NOT NULL,  -- Name of the technician who performed the maintenance
  `status` varchar(20) NOT NULL,  -- Status of the maintenance (e.g., Completed, Pending)
  PRIMARY KEY (`log_id`)  -- Primary key for the maintenance log table
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE `vendor_master` (
  `vendor_id` int NOT NULL AUTO_INCREMENT,  -- Unique identifier for the vendor
  `vendor_name` varchar(100) NOT NULL,  -- Name of the vendor
  `contact_person` varchar(100) NOT NULL,  -- Name of the primary contact person for the vendor
  `contact_phone` varchar(15) NOT NULL,  -- Phone number of the vendor's contact person
  `gst_number` varchar(20) NOT NULL,  -- GST number of the vendor (for tax purposes)
  `email` varchar(100) NOT NULL,  -- Email address of the vendor
  `address` varchar(200) NOT NULL,  -- Address of the vendor
  `city` varchar(100) NOT NULL,  -- City where the vendor is located
  `active_status` varchar(20) NOT NULL,  -- Vendor status (e.g., Active, Inactive)
  PRIMARY KEY (`vendor_id`)  -- Primary key for the vendor table
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
