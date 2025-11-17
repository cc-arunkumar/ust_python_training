
import csv

input_file = 'ust_healthcare_visits.csv'
pending_file = 'pending_payments.csv'
summary_file = 'patient_summary.csv'

required_field = ["patient_id", "name", "visit_date", "billed_amount", "payment_status","insurance_provider"]

clean_rows = []
skipped_row = 0
processed_row = 0
pending_count = 0
patient_summary = {}

with open(input_file, "r", newline="") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        # Skip rows missing required fields
        if not all(row.get(field) for field in required_field):
            print(f"Skipped due to missing required field: {row}")
            skipped_row += 1
            continue

        # Clean and normalize row values
        for key in row:
            try:
                row[key] = (row[key] or "").strip()
            except AttributeError:
                row[key] = str(row[key]).strip()

        # Convert billed_amount to float
        try:
            row["billed_amount"] = float(row["billed_amount"])
        except ValueError:
            skipped_row += 1
            print(f"Cannot convert billed_amount to float: {row}")
            continue
        row['payment_status'] = str(row["payment_status"]).lower().capitalize()

        clean_rows.append(row)

        # Build patient summary
        pid = str(row["patient_id"])
        if pid not in patient_summary:
            patient_summary[pid] = {
                "name": row["name"],
                "total_visit": 0,
                "total_billed": 0.0,
                "has_pending_payment": "No"
            }

        patient_summary[pid]["total_visit"] += 1
        patient_summary[pid]["total_billed"] += row["billed_amount"]

        if row["payment_status"] != "Paid":
            patient_summary[pid]["has_pending_payment"] = "Yes"

# Write pending payments
if clean_rows:
    with open(pending_file, mode="w", newline='') as file:
        fieldnames = [key for key in clean_rows[0] if key is not None]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in clean_rows:
            row = {k: v for k, v in row.items() if k is not None}
            if row["payment_status"] != "Paid":
                writer.writerow(row)
                pending_count += 1 
else:
    print("No pending payments. File not created.")

# Write patient summary
if patient_summary:
    with open(summary_file, mode="w", newline='') as file:
        fieldnames = ["patient_id", "name", "total_visit", "total_billed", "has_pending_payment"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for pid, data in patient_summary.items():
            writer.writerow({
                "patient_id": pid,
                "name": data["name"],
                "total_visit": data["total_visit"],
                "total_billed": f"{data['total_billed']:.2f}",
                "has_pending_payment": data["has_pending_payment"]
            })
            processed_row += 1
else:
    print("No patient summary generated.")

print(f"Skipped rows: {skipped_row}")
print(f"Processed rows: {processed_row}")
print(f"Pending payments: {pending_count}")



# =======sample output================
# skipped rows : 10
#processed rows: 91
#ending payments: 56


