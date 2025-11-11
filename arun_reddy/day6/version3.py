import csv

# Initialize counters
processed_rows = 0
skipped_rows = 0

# Required fields for validation
required_fields = ['patient_id', 'name', 'visit_date', 'department',
                   'billed_amount', 'insurance_provider', 'payment_status',
                   'contact', 'follow_up_required']

# Store cleaned rows and pending payments
cleaned_rows = []
pending_payments = []

# Read and clean data
with open("ust_healthcare_visits3.csv", "r", newline='') as file:
    reader = csv.DictReader(file)
    next(reader)
    
     # Iterating over the reader using the for loop 
    for row in reader:
        # Trim whitespace from all fields
        for key in row:
            if isinstance(row[key], str):
                row[key] = row[key].strip()

        # Normalize payment_status
        row["payment_status"] = row["payment_status"].title()

        # Normalize follow_up_required
        follow_up = row.get("follow_up_required", "").lower()
        row["follow_up_required"] = "Yes" if follow_up in ["yes", "y", "1", "true"] else "No"

        # Validate required fields and billed_amount together
        missing_data = False


       # iterating over the required fileds
        for field in required_fields:
            if field not in row or row[field] == "":
                missing_data = True
                break
        # using the try and catch 
        try:
            row["billed_amount"] = float(row["billed_amount"])
        except:
            missing_data = True

        if missing_data:
            print("Skipping row due to missing or invalid data:", row)
            skipped_rows += 1
            continue

        # Row is valid
        processed_rows += 1
        cleaned_rows.append(row)

        # Checking  for pending payments
        if row["payment_status"] != "Paid":
            pending_payments.append(row)

# Write pending_payments.csv
with open("pending_payments2.csv", "w", newline='') as file:
    header = ['patient_id', 'name', 'visit_date', 'department', 'billed_amount',
              'insurance_provider', 'payment_status', 'contact', 'follow_up_required']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for row in pending_payments:
        cleaned_row = {k: v for k, v in row.items() if k in header and k is not None}
        writer.writerow(cleaned_row)

# Create patient summary
patient_summary = {}

for row in cleaned_rows:
    pid = row["patient_id"]
    name = row["name"]
    billed = row["billed_amount"]
    status = row["payment_status"]

    if pid not in patient_summary:
        patient_summary[pid] = {
            "name": name,
            "visits": 1,
            "total_billed": billed,
            "has_pending": status != "Paid"
        }
    else:
        patient_summary[pid]["visits"] += 1
        patient_summary[pid]["total_billed"] += billed
        if status != "Paid":
            patient_summary[pid]["has_pending"] = True

# Write patient_summary.csv
with open("patient_summary2.csv", "w", newline='') as file:
    header = ["patient_id", "name", "total_visits", "total_billed", "has_pending_payment"]
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for pid, info in patient_summary.items():
        writer.writerow({
            "patient_id": pid,
            "name": info["name"],
            "total_visits": info["visits"],
            "total_billed": f"{info['total_billed']:.2f}",
            "has_pending_payment": "Yes" if info["has_pending"] else "No"
        })

# Final summary
print("Processed rows:", processed_rows)
print("Skipped rows:", skipped_rows)
print("pending_payments.csv rows:", len(pending_payments))
print("patient_summary.csv rows:", len(patient_summary))



# sample execution
# Skipping row due to missing or invalid data: {'patient_id': 'P003', 'name': '', 'visit_date': '2025/10/02', 'department': 'Neurology', 'billed_amount': 3500.0, 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': '8800123456', 'follow_up_required': 'No'}
# Skipping row due to missing or invalid data: {'patient_id': '', 'name': 'Meena Patel', 'visit_date': '2025-10-03', 'department': 'Cardiology', 'billed_amount': 2200.0, 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '7700123456', 'follow_up_required': 'No'}
# Skipping row due to missing or invalid data: {'patient_id': 'P005', 'name': 'Suresh K', 'visit_date': '2025-10-03', 'department': 'General Medicine', 'billed_amount': 'one thousand', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '9900112233', 'follow_up_required': 'Yes'}
# Skipping row due to missing or invalid data: {'patient_id': 'P009', 'name': 'Anita Singh', 'visit_date': '2025-10-05', 'department': 'General Medicine', 'billed_amount': 900.0, 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': '8800099999', 'follow_up_required': 'No'}
# Skipping row due to missing or invalid data: {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '2025-10-09', 'department': 'Cardiology', 'billed_amount': '₹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'Yes'}
# Skipping row due to missing or invalid data: {'patient_id': 'P023', 'name': 'Sana Khan', 'visit_date': '', 'department': 'Endocrinology', 'billed_amount': 3200.0, 'insurance_provider': 'EndoCare', 'payment_status': 'Paid', 'contact': '7700022222', 'follow_up_required': 'No'}
# Skipping row due to missing or invalid data: {'patient_id': 'P029', 'name': 'Liu Chen', 'visit_date': '2025-10-15', 'department': 'ENT', 'billed_amount': 'five thousand two hundred', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '6000012222', 'follow_up_required': 'Yes'}
# Skipping row due to missing or invalid data: {'patient_id': 'P040', 'name': 'Rachel Adams', 'visit_date': '2025-10-20', 'department': 'Endocrinology', 'billed_amount': '41OO.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 'contact': '7700035555', 'follow_up_required': 'No'}
# Skipping row due to missing or invalid data: {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '2025-10-09', 'department': 'Cardiology', 'billed_amount': '₹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'Yes'}
# Processed rows: 101
# Skipped rows: 9
# pending_payments.csv rows: 55
# patient_summary.csv rows: 90