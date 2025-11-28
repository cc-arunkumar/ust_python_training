# 📘 AIMS Plus
 
AIMS Plus is an **Asset & Inventory Management System** built with **FastAPI**.  
It provides RESTful APIs to manage assets, employees, maintenance logs, and vendors, with validation rules enforced using **Pydantic models**.
 
---
 
## 🚀 Features
- **Asset Management**: Create, update, search, list, and delete assets.
- **Employee Directory**: Manage employee records with validation rules.
- **Maintenance Logs**: Track repairs, services, and upgrades for assets.
- **Vendor Management**: Maintain vendor details with GST and contact validation.
- **Validation Layer**: Business rules enforced via Pydantic models.
 
---
 
## 🛠️ Tech Stack
- **Backend Framework**: FastAPI  
- **Database**: MySQL (via PyMySQL)  
- **ORM/Validation**: Pydantic  
- **Language**: Python 3.10+  
 
 
---
 
## 📂 Project Structure
AIMS_Plus/
│
├── database/
│   ├── create.sql
│   ├── sample_data/
│           |
│           ├── asset_inventory.csv
│           ├── employee_inventory.csv
│           ├── maintenance_log.csv
│           |── vendor_master.csv
│           │── final_data/
│                   ├── validated_asset_inventory.csv
│                   ├──  validated_employee_inventory.csv
│                   ├── validated_maintenance_log.csv
│                   └── validated_vendor_master.csv
│
├── src/
│   ├── api/
│   │   ├── asset_api.py
│   │   ├── employee_api.py
│   │   ├── vendor_api.py
│   │   └── maintenance_api.py
│   │
│   ├── crud/
│   │   ├── asset_crud.py
│   │   ├── employee_crud.py
│   │   ├── vendor_crud.py
│   │   └── maintenance_crud.py
│   │
│   ├── models/
│   │   ├── asset_model.py
│   │   ├── employee_model.py
│   │   ├── vendor_model.py
│   │   └── maintenance_model.py
│   │
│   ├── config/
│   │   └── db_connection.py
│   │
│   ├── exceptions/
│   │   └── custom_exceptions.py
│   │
│   ├── utils/
│   │   ├── validate_csv_data_util.py
│   │   └── dump_csv_data_util.py
│   │
│   ├── auth/
│   │   └── auth_jwt_token.py
│
│   └── main.py
│
└── README.md
 
**1. Configure Database**
 
- Update src/config/db_connection.py with your MySQL credentials:
conn = pymysql.Connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="ust_inventory_db",
    cursorclass=pymysql.cursors.DictCursor
)
 
 
 
**2.1 APIs for asset_inventory**
 
- POST /assets/create Create asset
- GET /assets/list Get all assets
- GET /assets/list?status= Filter by status
- GET /assets/{id} Get by asset_id
- PUT /assets/{id} Update full record
- PATCH /assets/{id}/status Update only status
- DELETE /assets/{id} Delete asset
- GET /assets/search?keyword=Search asset_tag, model,manufacturer
- GET /assets/count Count total assets
 
 
**2.2 APIs for employee_directory**
 
- POST /employees/create
- GET /employees/list
- GET /employees/list?status=
- GET /employees/{id}
- PUT /employees/{id}
- PATCH /employees/{id}/status
- DELETE /employees/{id}
- GET /employees/search?keyword=
- GET /employees/count
- POST /employees/bulk-upload
 
 
**2.3 APIs for vendor_master**
 
- POST /vendors/create
- GET /vendors/list
- GET /vendors/list?status=
- GET /vendors/{id}
- PUT /vendors/{id}
- PATCH /vendors/{id}/status
- DELETE /vendors/{id}
- GET /vendors/search?keyword=
- GET /vendors/count
 
 
**2.4 APIs for maintenance_log**
 
- POST /maintenance/create
- GET /maintenance/list
- GET /maintenance/list?status=
- GET /maintenance/{id}
- PUT /maintenance/{id}
- PATCH /maintenance/{id}/status
- DELETE /maintenance/{id}
- GET /maintenance/search?keyword=
- GET /maintenance/count