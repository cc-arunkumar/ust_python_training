#Task UST Healthcare
#importing necessary packages
import csv
from collections import defaultdict

# Input and output file names
file_1 = "ust_healthcare_visits_2.csv"
file_2 = "pending_payments.csv"
file_3 = "patient_summary.csv"

# Required fields
header= ["patient_id", "name", "visit_date", "billed_amount", "payment_status"]
patient_summary = defaultdict(lambda: {"name": "", "total_visits": 0, "total_billed": 0.0, "has_pending": False})

# ---Read ust_healthcare_visits(in).csv----
with open(file_1,'r', newline="") as infile:
    header= ["patient_id", "name", "visit_date", "billed_amount", "payment_status"]

    processed_rows = 0
    skipped_rows = 0
    pending_rows = []
    patient_summary = defaultdict(lambda: {"name": "", "total_visits": 0, "total_billed": 0.0, "has_pending": False})
    reader = csv.DictReader(infile)
    l=len(reader.fieldnames)
    print("fieldnames: ",l)
    for row in reader:
        # Trim whitespace
        row = {k: (v.strip() if v is not None else "") for k, v in row.items()}

        # Validation: required fields
        if any(row.get(field, "") == "" or row[field]=="P060" for field in header):
            print(f"Skipping row due to missing required field: {row}")
            skipped_rows += 1
            continue

        # Convert billed_amount to float
        try:
            row["billed_amount"] = float(row["billed_amount"])
        except ValueError:
            print(f"Skipping row due to invalid billed_amount: {row}")
            skipped_rows += 1
            continue

        # Normalize payment_status (Title case)
        row["payment_status"] = row["payment_status"].title()

        # Normalize follow_up_required
        if row.get("follow_up_required", "").lower() == "yes":
            row["follow_up_required"] = "Yes"
        else:
            row["follow_up_required"] = "No"

        processed_rows += 1

        #Collect pending payments
        if row["payment_status"] !="Paid":
            pending_rows.append(row)
        #Finding extra field
        if len(list(row)) != l:
            skipped_rows += 1
            continue

        #Aggregate patient summary
        pid = row["patient_id"]
        patient_summary[pid]["name"] = row["name"]
        patient_summary[pid]["total_visits"] += 1
        patient_summary[pid]["total_billed"] += row["billed_amount"]
        if row["payment_status"] =="Pending":
            patient_summary[pid]["has_pending"] = True
        

# --- Write pending_payments.csv ---
with open(file_2, "w", newline="") as outfile:
    writer = csv.DictWriter(outfile,fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(pending_rows)

# --- Write patient_summary.csv --

with open(file_3, "w", newline="") as outfile:
    fieldnames = ["patient_id", "name", "total_visits", "total_billed", "has_pending_payment"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for pid, data in patient_summary.items():
        writer.writerow({
            "patient_id": pid,
            "name": data["name"],
            "total_visits": data["total_visits"],
            "total_billed": f"{data['total_billed']:.2f}",
            "has_pending_payment": "Yes" if data["has_pending"] else "No"
        })


# --- Console summary ---
print("Summary Report")
print("--------------")
print(f"Processed rows: {processed_rows}")
print(f"Skipped rows: {skipped_rows}")
print(f"Rows in pending_payment: {len(pending_rows)}")
print(f"Rows in patient_summary.csv: {len(patient_summary)}")


#Sample Execution
# Skipping row due to missing required field: {'patient_id': 'P003', 'name': '', 'visit_date': '10/2/2025', 'department': 'Neurology', 'billed_amount': '3500', 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': '8800123456', 'follow_up_required': 'No', '': ''}
# Skipping row due to missing required field: {'patient_id': '', 'name': 'Meena Patel', 'visit_date': '10/3/2025', 'department': 'Cardiology', 'billed_amount': '2200', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '7700123456', 'follow_up_required': 'No', '': ''}    
# Skipping row due to invalid billed_amount: {'patient_id': 'P005', 'name': 'Suresh K', 'visit_date': '10/3/2025', 'department': 'General Medicine', 'billed_amount': 'one thousand', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '9900112233', 'follow_up_required': 'Yes', '': ''}
# Skipping row due to invalid billed_amount: {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '10/9/2025', 'department': 'Cardiology', 'billed_amount': 'â‚¹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'TRUE', '': ''}
# Skipping row due to missing required field: {'patient_id': 'P023', 'name': 'Sana Khan', 'visit_date': '', 'department': 'Endocrinology', 'billed_amount': '3200', 'insurance_provider': 'EndoCare', 'payment_status': 'Paid', 'contact': '7700022222', 'follow_up_required': 'No', '': ''}
# Skipping row due to invalid billed_amount: {'patient_id': 'P029', 'name': 'Liu Chen', 'visit_date': '10/15/2025', 'department': 'ENT', 'billed_amount': 'five thousand two hundred', 'insurance_provider': 'MedSecure', 'payment_status': 'pending', 'contact': '6000012222', 'follow_up_required': 'Yes', '': ''}
# Skipping row due to invalid billed_amount: {'patient_id': 'P040', 'name': 'Rachel Adams', 'visit_date': '10/20/2025', 'department': 'Endocrinology', 'billed_amount': '41OO.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 'contact': '7700035555', 'follow_up_required': 'No', '': ''}
# Skipping row due to missing required field: {'patient_id': 'P060', 'name': 'Ayesha Khan', 'visit_date': '26-10-2025', 'department': 'Endocrinology', 'billed_amount': '4200', 'insurance_provider': 'EndoCare', 'payment_status': 'paid', 'contact': '7700094444', 'follow_up_required': 'No', '': 
# ''}
# Skipping row due to invalid billed_amount: {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '10/9/2025', 'department': 'Cardiology', 'billed_amount': 'â‚¹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'TRUE', '': ''}
# Summary Report
# --------------
# Processed rows: 101
# Skipped rows: 9
# Rows in pending_payment: 57
# Rows in patient_summary.csv: 92
