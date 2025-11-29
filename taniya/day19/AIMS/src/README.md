#AIMS Plus

AIMS Plus is an **Asset & Inventory Management System** powered by **FastAPI**.  
It delivers RESTful APIs to handle assets, employees, maintenance records, and vendors, with strict validation enforced through **Pydantic models**.

---

## 🚀 Key Highlights
- **Asset Lifecycle Management**: Add, update, search, list, and remove assets.
- **Employee Directory**: Maintain employee records with validation rules.
- **Maintenance Tracking**: Log repairs, services, and upgrades for assets.
- **Vendor Registry**: Store vendor details with GST and contact checks.
- **Validation Layer**: Business rules enforced seamlessly via Pydantic.

---

## Technology Stack
- **Framework**: FastAPI  
- **Database**: MySQL (PyMySQL driver)  
- **Validation/ORM**: Pydantic  
- **Language**: Python 3.10+  

---

## Folder Layout
 AIMS_Plus/
│
├── database/
│   ├── create_tables.sql
│   ├── sample_data/
│   │   ├── asset_inventory.csv
│   │   ├── employee_directory.csv
│   │   ├── vendor_master.csv
│   │   └── maintenance_log.csv
│
├── src/
│   ├── config/
│   │   └── db_connection.py
│   │
│   ├── exceptions/
│   │   ├── custom_exceptions.py
│   │   └── exception_handler.py
│   │
│   ├── models/
│   │   ├── asset_model.py
│   │   ├── employee_model.py
│   │   ├── vendor_model.py
│   │   └── maintenance_model.py
│   │
│   ├── crud/
│   │   ├── asset_crud.py
│   │   ├── employee_crud.py
│   │   ├── vendor_crud.py
│   │   └── maintenance_crud.py
│   │
│   ├── api/
│   │   ├── asset_api.py
│   │   ├── employee_api.py
│   │   ├── vendor_api.py
│   │   └── maintenance_api.py
│   │
│   └── main.py
│
└── README.md


Code

---

##  Database Setup

Update `src/config/db_connection.py` with your MySQL credentials:

```python
conn = pymysql.Connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="ust_inventory_db",
    cursorclass=pymysql.cursors.DictCursor
)
📡 API Endpoints
1. Asset Inventory
POST /assets/create → Add new asset

GET /assets/list → List all assets

GET /assets/list?status= → Filter by status

GET /assets/{id} → Fetch asset by ID

PUT /assets/{id} → Update full record

PATCH /assets/{id}/status → Update only status

DELETE /assets/{id} → Remove asset

GET /assets/search?keyword= → Search by tag, model, manufacturer

GET /assets/count → Count total assets

2. Employee Directory
POST /employees/create

GET /employees/list

GET /employees/list?status=

GET /employees/{id}

PUT /employees/{id}

PATCH /employees/{id}/status

DELETE /employees/{id}

GET /employees/search?keyword=

GET /employees/count

POST /employees/bulk-upload

3. Vendor Master
POST /vendors/create

GET /vendors/list

GET /vendors/list?status=

GET /vendors/{id}

PUT /vendors/{id}

PATCH /vendors/{id}/status

DELETE /vendors/{id}

GET /vendors/search?keyword=

GET /vendors/count

4. Maintenance Log
POST /maintenance/create

GET /maintenance/list

GET /maintenance/list?status=

GET /maintenance/{id}

PUT /maintenance/{id}

PATCH /maintenance/{id}/status

DELETE /maintenance/{id}

GET /maintenance/search?keyword=

GET /maintenance/count
