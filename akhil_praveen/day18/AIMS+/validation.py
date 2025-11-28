# CSV module import for handling CSV files
import csv

# Importing the necessary models for the application from the src.models package
from src.models.assetsinventory import AssetInventory
from src.models.employeedirectory import EmployeeDirectory
from src.models.maintenancelog import MaintenanceLog
from src.models.vendormaster import VendorMaster

# Defining the base path for the CSV files
path = "C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/"

# Processing vendor master data from "vendor_master.csv" and saving to a new file
with open(path + "vendor_master.csv", "r") as vendor_file:
    # Open the final vendor file to write processed data
    with open(path + "final/vendor_master.csv", "w", newline="") as final_vendor_file:
        vendor_data = csv.DictReader(vendor_file)  # Reading the CSV as a dictionary
        header = vendor_data.fieldnames  # Getting the header (field names)
        new_vendor = csv.DictWriter(final_vendor_file, header[1:])  # Prepare to write without the "vendor_id"
        new_vendor.writeheader()  # Write the header to the final file
        
        # Looping through each row in the vendor data
        for data in vendor_data:
            try:
                # Trying to validate the data and create a VendorMaster object
                emp = VendorMaster(**data)
                del data["vendor_id"]  # Removing "vendor_id" as it's auto-generated in the database
                new_vendor.writerow(data)  # Writing the cleaned data to the new file
            except Exception as e:
                print(f"Error: {e}")
                print("Unable to process record")

# Processing employee directory data from "employee_directory.csv" and saving to a new file
with open(path + "employee_directory.csv", "r") as emp_file:
    # Open the final employee file to write processed data
    with open(path + "final/employee_directory.csv", "w", newline="") as final_emp_file:
        emp_data = csv.DictReader(emp_file)  # Reading the CSV as a dictionary
        header = emp_data.fieldnames  # Getting the header (field names)
        new_emp = csv.DictWriter(final_emp_file, header)  # Prepare to write the header as is
        new_emp.writeheader()  # Writing the header to the final file
        
        # Looping through each row in the employee data
        for data in emp_data:
            try:
                # Trying to validate the data and create an EmployeeDirectory object
                emp = EmployeeDirectory(**data)
                new_emp.writerow(data)  # Writing the validated data to the new file
            except Exception as e:
                print(f"Error: {e}")
                print("Unable to process record")

# Processing asset inventory data from "asset_inventory.csv" and saving to a new file
with open(path + "asset_inventory.csv", "r") as asset_file:
    # Open the final asset file to write processed data
    with open(path + "final/asset_inventory.csv", "w", newline="") as final_asset_file:
        asset_data = csv.DictReader(asset_file)  # Reading the CSV as a dictionary
        header = asset_data.fieldnames  # Getting the header (field names)
        new_asset = csv.DictWriter(final_asset_file, header)  # Prepare to write the header as is
        new_asset.writeheader()  # Writing the header to the final file
        
        # Looping through each row in the asset data
        for data in asset_data:
            try:
                # Trying to validate the data and create an AssetInventory object
                asset = AssetInventory(**data)
                new_asset.writerow(data)  # Writing the validated data to the new file
            except Exception as e:
                print(f"Error: {e}")  # Printing errors if data is invalid

# Processing maintenance log data from "maintenance_log.csv" and saving to a new file
with open(path + "maintenance_log.csv", "r") as maintain_file:
    # Open the final maintenance file to write processed data
    with open(path + "final/maintenance_log.csv", "w", newline="") as final_maintain_file:
        maintain_data = csv.DictReader(maintain_file)  # Reading the CSV as a dictionary
        header = maintain_data.fieldnames  # Getting the header (field names)
        new_maintain = csv.DictWriter(final_maintain_file, header[1:])  # Prepare to write without "log_id"
        new_maintain.writeheader()  # Writing the header to the final file
        
        # Looping through each row in the maintenance data
        for data in maintain_data:
            try:
                # Trying to validate the data and create a MaintenanceLog object
                emp = MaintenanceLog(**data)
                del data["log_id"]  # Removing "log_id" as it's auto-generated in the database
                new_maintain.writerow(data)  # Writing the cleaned data to the new file
            except Exception as e:
                print(f"Error: {e}")
                print("Unable to process record")
