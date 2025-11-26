CREATE TABLE `asset_inventory` (
  `asset_id` int NOT NULL AUTO_INCREMENT,
  `asset_tag` varchar(50) NOT NULL,
  `asset_type` varchar(50) NOT NULL,
  `serial_number` varchar(100) NOT NULL,
  `manufacturer` varchar(50) NOT NULL,
  `model` varchar(100) NOT NULL,
  `purchase_date` date NOT NULL,
  `warranty_years` int NOT NULL,
  `assigned_to` varchar(100) ,
  `asset_status` varchar(20) NOT NULL,
  `last_updated` datetime NOT NULL,
  PRIMARY KEY (`asset_id`),
  UNIQUE KEY ` asset_tag_UNIQUE` (`asset_tag`),
  UNIQUE KEY ` serial_number_UNIQUE` (`serial_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
