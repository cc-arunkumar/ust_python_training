import csv 
import re

error_list = []
answer_rows = []
valid_cities = ["Mumbai","Delhi","Bangalore","Chennai","Hyderabad","Pune","Kolkata"]

raw_vendor_file = r'C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\vendor_master(in).csv'
valid_vendor_file = r'C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\valid_vendors.csv'

with open(raw_vendor_file, mode='r', newline='',) as outfile:
    reader = csv.DictReader(outfile)
    all_fields = reader.fieldnames

    for row in reader:
        errors = []
        try:
            if not re.match(r"^[A-Za-z\s]{1,100}$", row["vendor_name"]):
                errors.append(f"Invalid vendor_name for vendor_id {row['vendor_id']}")

            if not re.match(r"^[A-Za-z\s]{1,100}$", row["contact_person"]):
                errors.append(f"Invalid contact_person for vendor_id {row['vendor_id']}")

            if not re.match(r"^[6-9]\d{9}$", row["contact_phone"]):
                errors.append(f"Invalid contact_phone for vendor_id {row['vendor_id']}")

            if not re.match(r"^[A-Za-z0-9]{15}$", row["gst_number"]):
                errors.append(f"Invalid gst_number for vendor_id {row['vendor_id']}")

            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", row["email"]):
                errors.append(f"Invalid email for vendor_id {row['vendor_id']}")

            if len(row["address"]) > 200:
                errors.append(f"Invalid address length for vendor_id {row['vendor_id']}")

            if row["city"] not in valid_cities:
                errors.append(f"Invalid city '{row['city']}' for vendor_id {row['vendor_id']}")

            if row["active_status"] not in ["Active", "Inactive"]:
                errors.append(f"Invalid active_status for vendor_id {row['vendor_id']}")
        except Exception as e:
            errors.append(f"Error: {e}")

        if not errors:
            answer_rows.append(row)
        else:
            error_list.append({"vendor_id": row["vendor_id"], "errors": errors})

# Write valid rows into new CSV
with open(valid_vendor_file, mode='w', newline='', encoding='utf-8') as file_out:
    writer = csv.DictWriter(file_out, fieldnames=all_fields)
    writer.writeheader()
    writer.writerows(answer_rows)

# print(len(answer_rows))
# print(len(error_list))