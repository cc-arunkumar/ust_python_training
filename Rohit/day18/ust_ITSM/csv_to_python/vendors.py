import csv 
from datetime import datetime
import re
error_list=[]
answer_rows = []
valid_cities = ["Mumbai","Delhi","Bangalore","Chennai","Hyderabad","Pune","Kolkata"]
cities_set = set()

with open (r'C:\Users\Administrator\Desktop\ust_python_training\Rohit\day18\ust_ITSM\data\vendor_master(in).csv',mode='r')as file2:
    reader=csv.DictReader(file2)
    all_fields=reader.fieldnames
    # for row in reader:
    #     cities_set.add(row["city"])
    
    for row in reader:
        errors=[]
        try:
            if not re.match(r"^[A-Za-z\s]{1,100}+$", row["vendor_name"]):
                val = f"Invalid vendor_name. Only alphabets and hhh spaces allowed and max 100 characters. {"Invalid vendor_name. Only alphabets and spaces allowed and max 100 characters.",row["vendor_id"]}"
                errors.append(val)
            
            if not re.match(r"^[A-Za-z\s]{1,100}+$", row["contact_person"]) :
                errors.append("Invalid contact_person. Only alphabets allowed and max 100 characters.")
            
            if  not re.match(r"^[6-9]\d{9}$", row["contact_phone"]):
                errors.append("Invalid contact_phone. Must be a 10-digit Indian mobile number starting with 6, 7, 8, or 9.")
            
            if not re.match(r"^[A-Za-z0-9]{15}$", row["gst_number"]):
                errors.append("Invalid gst_number. Must be exactly 15 alphanumeric characters.")
            
            if  not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", row["email"]):
                errors.append("Invalid email format.")
            
            if  len(row["address"]) > 200:
                errors.append("Invalid address. Address must be less than or equal to 200 characters.")
            
            if row["city"] not in valid_cities:
                errors.append(f"Invalid city. Must be one of the valid Indian cities. Given: {row['city']}")
            
            if row["active_status"] not in ["Active", "Inactive"]:
                errors.append("Invalid active_status. Must be 'Active' or 'Inactive'.")
        except Exception as e:
            errors.append(f"Error:{e}")
            
        
        if not errors:
            answer_rows.append(row)
            
            
print(errors)
print(len(errors))
# print(answer_rows) 
print(len(answer_rows))