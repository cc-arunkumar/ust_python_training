"""
Task Requirements
1. Read ust_healthcare_visits.csv with csv.DictReader .
2. Basic validation / normalization:
Required fields: patient_id , name , visit_date , billed_amount , payment_status . If any
missing → skip that row (and print a short message).
Convert billed_amount to float (if conversion fails, skip row).
Trim whitespace from string fields.
Normalize payment_status to Title case (e.g., "pending" → "Pending" ).
Normalize follow_up_required to "Yes" or "No" (treat empty as "No" ).
3. Create outputs:
pending_payments.csv : all cleaned columns for rows where payment_status != "Paid" .
patient_summary.csv : aggregated per patient_id with columns:
patient_id, name, total_visits, total_billed, has_pending_payment
total_billed formatted with 2 decimals (e.g., 7500.00 ).
has_pending_payment = "Yes" if any visit for that patient is not Paid;
otherwise "No" .
4. Console summary: print counts: processed rows, skipped rows, rows in each
output.

"""



import csv

# Assigning variables to CSV file names
details_file="DAY 6/tasks/ust_healthcare_visits.csv"
summary_file="DAY 6/tasks/patient_summary.csv"
pending_file="DAY 6/tasks/pending_payments.csv"

# Assigning variables for counting purpose
processes_rows=0
skipped_rows=0
pending_rows=0

# Storing of each data separately
cleaned_rows=[]
patient_rows={}

# Required fields
required_fields=["patient_id", "name", "visit_date", "billed_amount", "payment_status"]

# File normalization
with open(details_file,"r",encoding="utf-8") as ip_file:
    reader=csv.DictReader(ip_file)
    field_header=reader.fieldnames

    # Each row iteration
    for row in reader:
        processes_rows += 1

        # Remove None key 
        if None in row:
            print(f"Skipped due to Extra field in line {processes_rows}")
            skipped_rows += 1
            continue

        # REmoving whitespaces
        for key in row:
            if isinstance(row[key], str):
                row[key]=row[key].strip()

        # Checking missing required fields
        if any(not row.get(field) for field in required_fields):
            print(f"Skipped due to Missing required fields {processes_rows}")
            skipped_rows += 1
            continue

        # Converting billed_amount to float 
        try:
            row["billed_amount"] = round(float(row["billed_amount"]), 2)
        except ValueError:
            print(f"Skipped, there is invalid bill amount {processes_rows}")
            skipped_rows += 1
            continue

        # Normalizing string values
        if "payment_status" in row:
            row["payment_status"]= row["payment_status"].title()

        if "follow_up_required" in row:
            if len(row["follow_up_required"].strip())==0:
                row["follow_up_required"]="No"
            else:
                row["follow_up_required"]=row["follow_up_required"].title()
        else:
            row["follow_up_required"]="No"

        # Count pending payments
        if row["payment_status"]!="Paid":
            pending_rows+=1

        # Append cleaned data
        cleaned_rows.append(row)

# Pending Payments
with open(pending_file,"w", newline="",encoding="utf-8") as pen_file:
    writer=csv.DictWriter(pen_file, fieldnames=field_header)
    writer.writeheader()
    for row in cleaned_rows:
        writer.writerow(row)
    print("Pending payments created successfully")

# Patient Summary
with open(summary_file,"w",newline="",encoding="utf-8") as sum_file:
    writer = csv.DictWriter(sum_file, fieldnames=["patient_id", "name", "total_visits", "total_billed", "has_pending_payment"])
    writer.writeheader()

    for row in cleaned_rows:
        pid = row["patient_id"]

        if pid not in patient_rows:
            patient_rows[pid] = {
                "patient_id": pid,
                "name": row["name"],
                "total_visits": 0,
                "total_billed": 0.0,
                "has_pending_payment": "No"
            }

        patient_rows[pid]["total_visits"] += 1
        patient_rows[pid]["total_billed"] += float(row["billed_amount"])
        if row["payment_status"] != "Paid":
            patient_rows[pid]["has_pending_payment"] = "Yes"

    # Writing summarized data
    for pid, data in patient_rows.items():
        data["total_billed"] = f"{data['total_billed']:.2f}"
        writer.writerow(data)

    print("Patient summary created successfully.\n")

# final count
print(f"Number of processed rows:{len(cleaned_rows)}")
print(f"Number of skipped rows:{skipped_rows}")
print(f"Number of pending rows:{pending_rows}")
print(f"Total rows read:{processes_rows}")



"""
SAMPLE OUTPUT

Skipped due to Missing required fields 3
Skipped due to Missing required fields 4
Skipped, there is invalid bill amount 5
Skipped, there is invalid bill amount 16
Skipped due to Missing required fields 23
Skipped, there is invalid bill amount 29
Skipped, there is invalid bill amount 40
Skipped due to Extra field in line 52
Skipped, there is invalid bill amount 101
Pending payments created successfully
Patient summary created successfully.

Number of processed rows:101
Number of skipped rows:9
Number of pending rows:56
Total rows read:110

"""