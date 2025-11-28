import csv
from ..models.asset__model import AssetInventory
from datetime import datetime,date
from ..models.employee_model import Employee
from ..models.maintainence_model import Maintenence   
from ..models.vendor_model import Vendor
from ..exceptions.custom_exceptions import InvalidInputException,ValidationErrorException

# Lists to store valid and invalid records
processedassetlist = []
invalidassetlist = []

# Read asset data from CSV file
with open("C:\Users\Administrator\Desktop\AIMS_update\database\sampledata\asset_inventory.csv", "r") as file:
    content = csv.DictReader(file)
    for row in content:
        try:
            # Validate each row using Pydantic model
            asset = AssetInventory(**row)   

            # Add valid asset to processed list
            processedassetlist.append(asset)
        except InvalidInputException as e:
            invalidassetlist.append({"row": row, "error": str(e)})
        except ValidationErrorException as e:
            invalidassetlist.append({"row": row, "error": str(e)})
        except Exception as e:
            # Store invalid row along with error message
            invalidassetlist.append({"row": row, "error": str(e)})


# Write valid records into new CSV file
with open("asset_output.csv","w",newline="") as file:
    headers=["asset_tag","asset_type","serial_number","manufacturer","model","purchase_date","warranty_years","condition_status","assigned_to","location","asset_status"]
    content=csv.DictWriter(file,fieldnames=headers)
    content.writeheader()
    for asset in processedassetlist:
        # Write asset data as dictionary
        content.writerow(asset.__dict__)




# Lists to store valid and invalid employee records
processedemplist = []
invalidemplist = []

# Read employee data from CSV file
with open("C:\Users\Administrator\Desktop\AIMS_update\src\models\employee_model.py") as file:
    content=csv.DictReader(file)
    for row in content:
        try:
            # Validate each row using Pydantic Employee model
            asset = Employee(**row)   
            # Add valid employee to processed list
            processedemplist.append(asset)
        except InvalidInputException as e:
            invalidemplist.append({"row": row, "error": str(e)})
        except ValidationErrorException as e:
            invalidemplist.append({"row": row, "error": str(e)})
        except Exception as e:
            # Store invalid row along with error message
            invalidemplist.append({"row": row, "error": str(e)})

# Write valid employee records into new CSV file
with open("employee_output.csv","w",newline="") as file:
    headers=["emp_code","full_name","email","phone","department","location","join_date","status"]
    content=csv.DictWriter(file,fieldnames=headers)
    content.writeheader()
    for asset in processedemplist:
        # Write employee data as dictionary
        content.writerow(asset.__dict__)


# Lists to store valid and invalid maintenance records
processedmaintainlist = []
invalidmaintainlist = []

# Read maintenance log data from CSV file
with open("C:\Users\Administrator\Desktop\AIMS_update\database\sampledata\maintenance_log.csv", "r") as file:
    content = csv.DictReader(file)
    for row in content:
        try:
            # Validate each row using Pydantic Maintenence model
            asset = Maintenence(**row)
            # Add valid record to processed list
            processedmaintainlist.append(asset)
        except InvalidInputException as e:
            invalidmaintainlist.append({"row": row, "error": str(e)})
        except ValidationErrorException as e:
            invalidmaintainlist.append({"row": row, "error": str(e)})
        except Exception as e:
            # Store invalid row along with error message
            invalidmaintainlist.append({"row": row, "error": str(e)})

# Write valid maintenance records into new CSV file
with open("maintainence_output.csv","w",newline="") as file:
    headers=["log_id","asset_tag","maintenance_type","vendor_name","description","cost","maintenance_date","technician_name","status"]
    content=csv.DictWriter(file,fieldnames=headers)
    content.writeheader()
    for asset in processedmaintainlist:
        # Write maintenance record data as dictionary
        content.writerow(asset.__dict__)


# Lists to store valid and invalid vendor records
processedvendorlist = []
invalidvendorlist = []

# Read vendor data from CSV file
with open("C:\Users\Administrator\Desktop\AIMS_update\database\sampledata\vendor_master.csv", "r") as file:
    content = csv.DictReader(file)
    for row in content:
        try:
            # Validate each row using Pydantic Vendor model
            asset = Vendor(**row) 
            # Add valid vendor record to processed list
            processedvendorlist.append(asset)
        except InvalidInputException as e:
            # Store invalid row along with error message
            invalidvendorlist.append({"row": row, "error": str(e)})
        except ValidationErrorException as e:
            invalidvendorlist.append({"row":row,"error":str(e)})
        except Exception as e:
            invalidvendorlist.append({"row":row,"error":str(e)})
            


# Write valid vendor records into new CSV file
with open("C:/Users/Administrator/Desktop/AIMS_update/database/sampleoutput/vendor_output.csv","w",newline="") as file:
    headers=["vendor_id","vendor_name","contact_person","contact_phone","gst_number","email","address","city","active_status"]
    content = csv.DictWriter(file, fieldnames=headers)
    content.writeheader()
    for asset in processedvendorlist:
        # Write vendor data as dictionary
        content.writerow(asset.__dict__)
