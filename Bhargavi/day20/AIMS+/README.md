AIMS Plus

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

Language: Python 3.10+

Project Structure
AIMS_Plus/
│
├── database/
│   ├── create.sql
│   ├── sample_data/
│   │   ├── asset_inventory.csv
│   │   ├── employee_inventory.csv
│   │   ├── maintenance_log.csv
│   │   └── vendor_master.csv
│   ├── final_data/
│   │   ├── validated_asset_inventory.csv
│   │   ├── validated_employee_inventory.csv
│   │   ├── validated_maintenance_log.csv
│   │   └── validated_vendor_master.csv
│
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

Configuration
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

POST /assets/create — Create a new asset.

GET /assets/list — Get all assets.

GET /assets/list?status= — Filter by asset status.

GET /assets/{id} — Get asset by asset_id.

PUT /assets/{id} — Update full asset record.

PATCH /assets/{id}/status — Update asset status only.

DELETE /assets/{id} — Delete asset.

GET /assets/search?keyword= — Search by asset_tag, model, or manufacturer.

GET /assets/count — Get the total number of assets.

2.2 APIs for Employee Directory

POST /employees/create — Create a new employee record.

GET /employees/list — Get a list of all employees.

GET /employees/list?status= — Filter by employee status.

GET /employees/{id} — Get employee details by id.

PUT /employees/{id} — Update employee details.

PATCH /employees/{id}/status — Update employee status only.

DELETE /employees/{id} — Delete employee record.

GET /employees/search?keyword= — Search employees by name or job title.

GET /employees/count — Get the total number of employees.

POST /employees/bulk-upload — Upload multiple employee records via CSV.

2.3 APIs for Vendor Master

POST /vendors/create — Add a new vendor.

GET /vendors/list — Get a list of all vendors.

GET /vendors/list?status= — Filter by vendor status.

GET /vendors/{id} — Get vendor details by id.

PUT /vendors/{id} — Update vendor details.

PATCH /vendors/{id}/status — Update vendor status only.

DELETE /vendors/{id} — Delete vendor record.

GET /vendors/search?keyword= — Search vendors by name or contact.

GET /vendors/count — Get the total number of vendors.

2.4 APIs for Maintenance Log

POST /maintenance/create — Create a maintenance log.

GET /maintenance/list — Get all maintenance logs.

GET /maintenance/list?status= — Filter maintenance logs by status.

GET /maintenance/{id} — Get maintenance log by id.

PUT /maintenance/{id} — Update maintenance log.

PATCH /maintenance/{id}/status — Update maintenance status only.

DELETE /maintenance/{id} — Delete maintenance log.

GET /maintenance/search?keyword= — Search maintenance logs by description or asset ID.

GET /maintenance/count — Get the total number of maintenance logs.