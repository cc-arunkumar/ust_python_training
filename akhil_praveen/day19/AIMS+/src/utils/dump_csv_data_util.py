import csv
from ..crud.asset_crud import AssetCrud
from ..crud.employee_crud import EmployeeCrud
from ..crud.maintenance_crud import MaintenanceCrud
from ..crud.vendor_crud import VendorCrud

# Open the CSV file containing asset data
with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/asset_inventory.csv", "r") as asset_file:
    csv_file = csv.DictReader(asset_file)
    
    # Iterate over each row in the CSV file and insert it into the database
    for data in csv_file:
        AssetCrud.create_asset(data)
 
# Open the CSV file containing employee data       
with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/employee_directory.csv","r") as employee_file:
    csv_file = csv.DictReader(employee_file)
    
    for data in csv_file:
        EmployeeCrud.create_employee(data)
        
        
# Open the CSV file containing maintenance data
with open("path/to/maintenance_log.csv","r") as maintenance_file:
    csv_file = csv.DictReader(maintenance_file)
    for data in csv_file:
        MaintenanceCrud.create_maintenance(data)
        

# Open the CSV file containing vendor data
with open("path/to/vendor_master.csv","r") as vendor_file:
    csv_file = csv.DictReader(vendor_file)
    for data in csv_file:
        VendorCrud.create_vendor(data)