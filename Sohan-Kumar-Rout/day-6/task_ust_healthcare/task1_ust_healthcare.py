#Task 1 : UST Healthcare 

import csv
from collections import defaultdict

# Input and output file names
file_input = "ust_healthcare_visits(in)_2.csv"
file_pending_details = "pending_payment_file.csv"
file_summary = "patient_summary_file.csv"

# Recquired fields
header =["patient_id","name","visit_date","billed_amount","payment_status"]
patient_summary=defaultdict(lambda : {"name " : "", "total_visits" : 0,"total_billed" : 0.0,"has_pending" : False})



# Read and clean data
with open(file_input, "r", newline='') as file:
    header  = ["patient_id","name","visit_date","billed_amount","payment_status"]    
    processed_rows=0
    skipped_rows=0
    pending_rows=[]
    patient_summary=defaultdict(lambda : {"name" : "", "total_visits" : 0, "total_billed": 0.0, "has_pending" : False})
    reader = csv.DictReader(file)
    for row in reader:
        
        # Trim white spaces 
        for key in row:
            if row[key]==str:
                row[key]=row[key].strip()
        if "patient_id" not in row or 'name' not in row or 'visit_date' not in row or 'billed_amount' not in row or 'payment_status' not in row:
            print(f"Skipped row due to missing required field : {row}")
            skipped_rows+=1
            continue
        if not row.get('insurance_provider') or not row.get('visit_date'):
            skipped_rows+=1
            print(f"Skipped row due to missing required field : {row}")
            continue
    
        try:
            if(len(row['name'])>0 and float(row['billed_amount'])):
                row['billed_amount']=float(row["billed_amount"])
        except:
            print(f"Skipped row due to invalid bill amount {row}")
            skipped_rows+=1
            continue

        # Normalize payment status
        row["payment_status"] = row["payment_status"].title()

        # follow-up status from extra fields
        if row.get("follow_up_required"," ").lower() =="yes":
            row["follow_up_required"]="Yes"
        else:
            row["follow_up_required"]="No"

        processed_rows+=1
        
        if row["payment_status"]!="Paid":
            pending_rows.append(row)
        

        # Patient summary
        pid = row["patient_id"]
        patient_summary[pid]["name"] = row["name"]
        patient_summary[pid]["total_visits"] += 1
        patient_summary[pid]["total_billed"] += row["billed_amount"]
        if row["payment_status"] == "Pending":
            patient_summary[pid]["has_pending"] = True


# Write pending payment.csv
with open(file_pending_details,"w",newline="") as outfile:
    writer=csv.DictWriter(outfile,fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(pending_rows)
# Write patient summary.csv
with open(file_summary,"w", newline="") as outfile:
    fieldnames=["patient_id","name","total_visits","total_billed","has_pending"]
    writer=csv.DictWriter(outfile,fieldnames=fieldnames)
    writer.writeheader()
    for pid,data in patient_summary.items():
        writer.writerow({
            "patient_id" : pid,
            "name" : data["name"],
            "total_visits": data["total_visits"],
            "total_billed" : f"{data['total_billed']:.2f}",
            "has_pending" : "Yes" if data["has_pending"] else "No"
        })
#Summary report 

print("Summary Report")
print("---------------")
print(f"Processed rows : {processed_rows}")
print(f"Skipped rows : {skipped_rows}")
print(f"Rows in pending_payment : {len(pending_rows)}")
print(f"Rows in patient summary : {len(patient_summary)}")

#Output
# Skipped row due to missing required field : {'patient_id': 'P003', 'name': ' ', 'visit_date': '10/2/2025', 'department': 'Neurology', 'billed_amount': '3500', 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': 
# '8800123456', 'follow_up_required': 'No', '': ''}
# Skipped row due to invalid bill amount {'patient_id': 'P005', 'name': 'Suresh K', 'visit_date': '10/3/2025', 'department': 'General Medicine', 'billed_amount': 'one thousand', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '9900112233', 'follow_up_required': 'Yes', '': ''}
# Skipped row due to missing required field : {'patient_id': 'P009', 'name': 'Anita Singh', 'visit_date': '10/5/2025', 'department': 'General Medicine', 'billed_amount': '900', 'insurance_provider': '', 'payment_status': 'unPaid', 'contact': '8800099999', 'follow_up_required': 'n', '': ''}
# Skipped row due to invalid bill amount {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '10/9/2025', 'department': 'Cardiology', 'billed_amount': 'â‚¹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'TRUE', '': ''}
# Skipped row due to missing required field : {'patient_id': 'P022', 'name': 'Tom Hanks', 'visit_date': '10/12/2025', 'department': 'Neurology', 'billed_amount': '5000', 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': '8800088888', 'follow_up_required': 'No', '': ''}
# Skipped row due to missing required field : {'patient_id': 'P023', 'name': 'Sana Khan', 'visit_date': '', 'department': 'Endocrinology', 'billed_amount': '3200', 'insurance_provider': 'EndoCare', 'payment_status': 'Paid', 'contact': '7700022222', 'follow_up_required': 'No', '': ''}
# Skipped row due to invalid bill amount {'patient_id': 'P029', 'name': 'Liu Chen', 'visit_date': '10/15/2025', 'department': 'ENT', 'billed_amount': ' five thousand two hundred ', 'insurance_provider': 'MedSecure', 'payment_status': ' pending ', 'contact': '6000012222', 'follow_up_required': 'Yes', '': ''}
# Skipped row due to invalid bill amount {'patient_id': 'P040', 'name': 'Rachel Adams', 'visit_date': '10/20/2025', 'department': 'Endocrinology', 'billed_amount': '41OO.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 'contact': '7700035555', 'follow_up_required': 'No', '': ''}
# Skipped row due to invalid bill amount {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '10/9/2025', 'department': 'Cardiology', 'billed_amount': 'â‚¹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'TRUE', '': ''}
# Summary Report
# ---------------
# Processed rows : 101
# Skipped rows : 9
# Rows in pending_payment : 58
# Rows in patient summary : 92
