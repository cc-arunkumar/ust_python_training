CREATE TABLE ust_asset_db.asset_inventory (
    asset_id INT PRIMARY KEY AUTO_INCREMENT,
    asset_tag VARCHAR(50) UNIQUE NOT NULL,
    asset_type VARCHAR(50) NOT NULL,
    serial_number VARCHAR(100) UNIQUE NOT NULL,
    manufacturer VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    purchase_date DATE NOT NULL,
    warranty_years INT NOT NULL CHECK (warranty_years > 0),
    assigned_to VARCHAR(100) NULL,
    asset_status VARCHAR(20) NOT NULL CHECK (asset_status IN ('Available', 'Assigned', 'Repair', 'Retired')),
    last_updated DATETIME NOT NULL
);

DELIMITER $$
CREATE TRIGGER ust_asset_db.trg_asset_inventory_update
BEFORE UPDATE ON ust_asset_db.asset_inventory
FOR EACH ROW
BEGIN
    SET NEW.last_updated = NOW();
END$$
DELIMITER ;