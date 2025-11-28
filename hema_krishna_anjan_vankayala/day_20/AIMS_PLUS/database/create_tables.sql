CREATE TABLE `asset_inventory` (
  `asset_id` int NOT NULL AUTO_INCREMENT,
  `asset_tag` varchar(50) NOT NULL,
  `asset_type` varchar(50) NOT NULL,
  `serial_number` varchar(100) NOT NULL,
  `manufacturer` varchar(50) NOT NULL,
  `model` varchar(100) NOT NULL,
  `purchase_date` date NOT NULL,
  `warranty_years` int NOT NULL,
  `condition_status` varchar(20) NOT NULL,
  `assigned_to` varchar(150) DEFAULT NULL,
  `location` varchar(100) NOT NULL,
  `asset_status` varchar(20) NOT NULL,
  `last_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`asset_id`),
  UNIQUE KEY `serial_number` (`serial_number`)
)

