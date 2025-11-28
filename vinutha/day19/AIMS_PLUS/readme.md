AIMS Plus - Asset & Inventory Management System

AIMS Plus is an Asset & Inventory Management System built with FastAPI. It provides RESTful APIs to manage assets, employees, maintenance logs, and vendors, with validation rules enforced using Pydantic models.

Features

Asset Management: Create, update, search, list, and delete assets.

Employee Directory: Manage employee records with validation rules.

Maintenance Logs: Track repairs, services, and upgrades for assets.

Vendor Management: Maintain vendor details with GST and contact validation.

Validation Layer: Business rules enforced via Pydantic models.

Tech Stack

Backend Framework: FastAPI
Database: MySQL (via PyMySQL)
ORM/Validation: Pydantic
Programming Language: Python 3.10+

Project Structure

AIMS_Plus/
├── database/
│   ├── create.sql
│   ├── sample_data/
│   │   ├── asset_inventory.csv
│   │   ├── employee_inventory.csv
│   │   ├── maintenance_log.csv
│   │   ├── vendor_master.csv
│   └── final_data/
│       ├── validated_asset_inventory.csv
│       ├── validated_employee_inventory.csv
│       ├── validated_maintenance_log.csv
│       └── validated_vendor_master.csv
├── src/
│   ├── api/
│   │   ├── asset_api.py
│   │   ├── employee_api.py
│   │   ├── vendor_api.py
│   │   └── maintenance_api.py
│   ├── crud/
│   │   ├── asset_crud.py
│   │   ├── employee_crud.py
│   │   ├── vendor_crud.py
│   │   └── maintenance_crud.py
│   ├── models/
│   │   ├── asset_model.py
│   │   ├── employee_model.py
│   │   ├── vendor_model.py
│   │   └── maintenance_model.py
│   ├── config/
│   │   └── db_connection.py
│   ├── exceptions/
│   │   └── custom_exceptions.py
│   ├── utils/
│   │   ├── validate_csv_data_util.py
│   │   └── dump_csv_data_util.py
│   ├── auth/
│   │   └── auth_jwt_token.py
│   └── main.py
└── README.md


Setup Instructions
1. Configure Database

Update src/config/db_connection.py with your MySQL credentials:

conn = pymysql.Connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="ust_inventory_db",
    cursorclass=pymysql.cursors.DictCursor
)

API Endpoints
2.1 APIs for Asset Inventory

POST /assets/create: Create a new asset.

GET /assets/list: Get all assets.

Query: GET /assets/list?status=<status> (Filter by asset status)

GET /assets/{id}: Get asset by asset_id.

PUT /assets/{id}: Update the full asset record.

PATCH /assets/{id}/status: Update only the asset's status.

DELETE /assets/{id}: Delete an asset.

GET /assets/search?keyword=<keyword>: Search by asset_tag, model, manufacturer.

GET /assets/count: Get the total count of assets.

2.2 APIs for Employee Directory

POST /employees/create: Add a new employee.

GET /employees/list: Get all employees.

Query: GET /employees/list?status=<status> (Filter by employee status)

GET /employees/{id}: Get employee by emp_id.

PUT /employees/{id}: Update an employee's record.

PATCH /employees/{id}/status: Update only the employee's status.

DELETE /employees/{id}: Delete an employee.

GET /employees/search?keyword=<keyword>: Search by employee name or ID.

GET /employees/count: Get the total count of employees.

POST /employees/bulk-upload: Bulk upload employee data.

2.3 APIs for Vendor Master

POST /vendors/create: Add a new vendor.

GET /vendors/list: Get all vendors.

Query: GET /vendors/list?status=<status> (Filter by vendor status)

GET /vendors/{id}: Get vendor by id.

PUT /vendors/{id}: Update vendor details.

PATCH /vendors/{id}/status: Update only the vendor's status.

DELETE /vendors/{id}: Delete a vendor.

GET /vendors/search?keyword=<keyword>: Search by vendor name or contact.

GET /vendors/count: Get the total count of vendors.

2.4 APIs for Maintenance Logs

POST /maintenance/create: Create a maintenance log entry.

GET /maintenance/list: Get all maintenance logs.

Query: GET /maintenance/list?status=<status> (Filter by log status)

GET /maintenance/{id}: Get maintenance log by id.

PUT /maintenance/{id}: Update a maintenance log entry.

PATCH /maintenance/{id}/status: Update only the maintenance log's status.

DELETE /maintenance/{id}: Delete a maintenance log entry.

GET /maintenance/search?keyword=<keyword>: Search by asset ID or log details.

GET /maintenance/count: Get the total count of maintenance logs.