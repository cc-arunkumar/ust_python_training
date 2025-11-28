from models import asset_model,employee_model,vendor_model,maintenance_model
import csv

def validate_asset_data():
    updated_file = []
    errors_list = []
    with open('../database/sample_data/asset_inventory.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                new_asset = asset_model.AssetInventory(**row)
                updated_file.append(row)
            except Exception as e:
                new_err = {**row}
                new_err['Error'] = e
                errors_list.append(new_err)
    print(len(errors_list))
    
    with open('../database/sample_data/final/validated_asset_directory.csv','w',newline="") as file:
        headers = ['asset_tag','asset_type','serial_number','manufacturer','model','purchase_date','warranty_years','condition_status','assigned_to','location','asset_status']

        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_file)
        
    with open('../database/sample_data/final/error_asset_directory.csv','w',newline="") as file:
        headers = ['asset_tag','asset_type','serial_number','manufacturer','model','purchase_date','warranty_years','condition_status','assigned_to','location','asset_status','Error']

        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(errors_list)
        
def validate_employee_data():
    updated_file = []
    errors_list = []
    with open('../database/sample_data/employee_directory.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                new_asset = employee_model.EmployeeDirectory(**row)
                updated_file.append(row)
            except Exception as e:
                new_err = {**row}
                new_err['Error'] = e
                errors_list.append(new_err)
    print(len(errors_list))
    
    with open('../database/sample_data/final/validated_employee_directory.csv','w',newline="") as file:
        headers = ['emp_code','full_name','email','phone','department','location','join_date','status']

        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_file)
        
    with open('../database/sample_data/final/error_employee_directory.csv','w',newline="") as file:
        headers = ['emp_code','full_name','email','phone','department','location','join_date','status','Error']

        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(errors_list)
        
def validate_maintenance_data():
    updated_file = []
    errors_list = []
    with open('../database/sample_data/maintenance_log.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                new_asset = maintenance_model.MaintenanceLog(**row)
                updated_file.append(row)
            except Exception as e:
                new_err = {**row}
                new_err['Error'] = e
                errors_list.append(new_err)
    print(len(errors_list))
    
    with open('../database/sample_data/final/validated_maintenance_log.csv','w',newline="") as file:
        headers = ['log_id','asset_tag','maintenance_type','vendor_name','description','cost','maintenance_date','technician_name','status']

        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_file)
        
    with open('../database/sample_data/final/error_maintenance_log.csv','w',newline="") as file:
        headers = ['log_id','asset_tag','maintenance_type','vendor_name','description','cost','maintenance_date','technician_name','status','Error']

        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(errors_list)
        

def validate_vendor_data():
    updated_file = []
    errors_list = []
    with open('../database/sample_data/vendor_master.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                new_asset = vendor_model.VendorMaster(**row)
                updated_file.append(row)
            except Exception as e:
                new_err = {**row}
                new_err['Error'] = e
                errors_list.append(new_err)
    print(len(errors_list))
    
    with open('../database/sample_data/final/validated_vendor_master.csv','w',newline="") as file:
        headers = ['vendor_id','vendor_name','contact_person','contact_phone','gst_number','email','address','city','active_status']
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(updated_file)
        
    with open('../database/sample_data/final/error_vendor_master.csv','w',newline="") as file:
        headers = ['vendor_id','vendor_name','contact_person','contact_phone','gst_number','email','address','city','active_status','Error']
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(errors_list)