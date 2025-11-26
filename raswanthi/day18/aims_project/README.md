# 🖥️ Asset Inventory Management System (AIMS)

AIMS is a simple Python + MySQL project to manage IT assets (laptops, monitors, docking stations, keyboards, mice).  
It demonstrates **CRUD Operations** with validation rules and a clean modular structure.

---

Project Structure ->

AIMS_Project/
 │ ├── src/ 
 │ ├── config/ 
 │ │ └── db_connection.py # MySQL connection setup 
 │ │ │ ├── helpers/ 
 │ │ └── validators.py # Input validation rules 
 │ │ │ ├── crud/ 
 │ │ └── asset_crud.py # CRUD functions (create, read, update, delete) 
 │ │ │ └── main.py # Demo runner for CRUD operations 
 │ └── README.md # Documentation