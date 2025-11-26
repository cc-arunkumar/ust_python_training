# Asset Inventory Management System

## Overview

The **Asset Inventory Management System** is a Python-based application designed to manage the inventory of various assets. The system allows you to create, read, update, and delete asset records in a database. The project also logs each action to a file for tracking purposes, ensuring better management and accountability of assets within an organization.

---

## Features

- **Create**: Add new assets to the inventory.
- **Read**: Retrieve asset details by asset ID or retrieve all assets.
- **Update**: Modify asset details, including status, manufacturer, model, etc.
- **Delete**: Remove assets from the inventory by their asset ID.
- **Validation**: Ensure asset data (such as asset tag, serial number, and status) is valid before performing operations.
- **Logging**: Track all asset-related actions and errors in a log file (`app.log`).
  
---

## Project Structure

The project is organized into several directories and files for better modularity and maintainability:

```
Asset-Inventory-Management-System/
│
├── config/
│   └── db_connection.py             # Handles the database connection setup
├── crud/
│   └── asset_crud.py                # Contains CRUD operations for asset management
├── helpers/
│   └── validators.py                # Validates inputs for asset operations
├── logs/
│   └── app.log                      # Log file tracking all operations and errors
├── README.md                        # This file
├── requirements.txt                 # List of Python dependencies
└── main.py                          # Script to run asset CRUD operations
```

---

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**
- **MySQL** or another relational database

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/asset-inventory-management.git
```

### Step 2: Install Dependencies

Navigate to the project directory and install the required Python packages using the following command:

```bash
cd asset-inventory-management
pip install -r requirements.txt
```

The `requirements.txt` file contains necessary dependencies like `mysql-connector` for connecting to the database.

### Step 3: Configure the Database

1. **Create a Database**:
   
   Run the following SQL commands to create the `asset_inventory` database and a table for storing asset information:

```sql
CREATE DATABASE asset_inventory;

USE asset_inventory;

CREATE TABLE asset_inventory (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_tag VARCHAR(255) UNIQUE NOT NULL,
    asset_type VARCHAR(50),
    serial_number VARCHAR(255) UNIQUE NOT NULL,
    manufacturer VARCHAR(100),
    model VARCHAR(100),
    purchase_date DATE,
    warranty_years INT,
    assigned_to VARCHAR(100),
    asset_status VARCHAR(50),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

2. **Update Database Connection**:

   Update your database connection details in `config/db_connection.py` to match your MySQL server credentials.

```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your-username",  # Replace with your MySQL username
        password="your-password",  # Replace with your MySQL password
        database="asset_inventory"
    )
```

---

## Usage

### Main Operations

Here’s how to use the system to manage assets:

1. **Create an Asset**:
   ```python
   result = create_asset(
       asset_tag="UST-LTP-1001",
       asset_type="Laptop",
       serial_number="SN-ABC12345",
       manufacturer="HP",
       model="HP EliteBook 850",
       purchase_date="2023-06-15",
       warranty_years=3,
       assigned_to=None,
       asset_status="Available"
   )
   print(result)
   ```

2. **Read All Assets**:
   ```python
   read_all_assets()  # Retrieve and print all assets in the inventory
   ```

3. **Read an Asset by ID**:
   ```python
   read_asset_by_id(1)  # Retrieve and print asset with ID 1
   ```

4. **Update an Asset**:
   ```python
   result = update_asset(
       asset_id=1,
       asset_type="Laptop",
       manufacturer="Dell",
       model="Dell XPS 15",
       warranty_years=4,
       asset_status="Assigned",
       assigned_to="John Doe (UST Bangalore)"
   )
   print(result)
   ```

5. **Delete an Asset**:
   ```python
   result = delete_asset(2)  # Delete asset with ID 2
   print(result)
   ```

---

## Logging

The system logs all actions and errors in the `logs/app.log` file, which tracks important operations like asset creation, updates, and deletions. Logs are written with a timestamp and provide insights into system activity.

**Example Log Output:**

```
2025-11-26 14:30:45 - DEBUG - Attempting to create asset with tag: UST-LTP-1001, serial: SN-ABC12345
2025-11-26 14:30:45 - INFO - Asset created successfully with ID: 101, Tag: UST-LTP-1001, Status: Available
```

---

## Error Handling

The system includes comprehensive error handling:

- **Validation Errors**: If an asset tag, serial number, or other fields don't meet the required criteria, appropriate error messages will be raised.
- **CRUD Errors**: If any database operation fails, the system logs the error and provides a meaningful error message.
- **Asset Not Found**: If an asset doesn't exist (when updating or deleting), the system logs a warning and informs the user.

---

## Dependencies

This project relies on the following dependencies:
- **mysql-connector-python**: To interact with MySQL databases.
- **logging**: For tracking system activity.
- **os**: For file and directory operations.

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- **Asset Categories**: Add more asset categories, like printers, projectors, etc.
- **User Management**: Implement user authentication and role-based access.
- **Asset Location**: Add location management to track where each asset is assigned.
- **Reports**: Generate detailed reports on asset usage, status, and warranty.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### Contact

For any questions or issues, feel free to reach out to the project maintainers or open an issue on the GitHub repository.
