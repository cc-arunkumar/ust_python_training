import csv
# File paths
INPUT_FILE = "ust_healthcare_visits (1).csv"
OUTPUT_FILE = "pending_payments.csv"
PATIENT_FILE = "patient_summary.csv"

REQUIRED_FIELDS = ['patient_id', 'name', 'visit_date', 'billed_amount', 'payment_status']

# Counters and storage
processed_rows = 0
skipped_rows = 0
pending_rows = []
patient_summary = {}  

# Helper: normalize payment status
def normalize_status(raw_status: str) -> str:
    raw = raw_status.strip().lower()
    if raw in ("", "no"):
        return "No"
    elif raw in ("pending", "yes"):
        return "Pending"
    elif raw == "paid":
        return "Paid"
    else:
        return raw_status.strip().title()


# Helper: validate row
def is_valid_row(row):
    missing = [f for f in REQUIRED_FIELDS if not row.get(f) or not row[f].strip()]
    return not missing, missing

# Step 3: Read input CSV
with open(INPUT_FILE, newline="") as infile:
    reader = csv.DictReader(infile)
    all_fields = reader.fieldnames

    for row in reader:
        # Skip invalid rows
        valid, missing = is_valid_row(row)
        if None in row or not valid:
            print(f"Skipping row (missing fields {missing}):", row)
            skipped_rows += 1
            continue

        try:
            billed_amount = float(row["billed_amount"].strip())
        except ValueError:
            print("Skipping row (invalid billed_amount):", row)
            skipped_rows += 1
            continue

        # Cleaned values
        patient_id = row["patient_id"]
        name = row["name"].strip()
        visit_date = row["visit_date"].strip()
        payment_status = normalize_status(row["payment_status"])

        cleaned_row = {
            "patient_id": patient_id,
            "name": name,
            "visit_date": visit_date,
            "billed_amount": f"{billed_amount:.2f}",
            "payment_status": payment_status
        }

        # Initialize patient summary if not present
        if patient_id not in patient_summary:
            patient_summary[patient_id] = {
                "name": name,
                "total_visits": 0,
                "total_billed": 0.0,
                "has_pending_payment": False
            }

        # Update patient summary
        summary = patient_summary[patient_id]
        summary["name"] = name
        summary["total_visits"] += 1
        summary["total_billed"] += billed_amount
        if payment_status == "Pending":
            summary["has_pending_payment"] = True

        # Collect pending payments
        if payment_status == "Pending":
            summary["has_pending_payment"] = True

        if payment_status == "Paid":
            pass
        else:
            pending_rows.append(cleaned_row)

        processed_rows += 1

# Step 6: Write patient summary
with open(PATIENT_FILE, "w", newline="") as outfile:
    fieldnames = ["patient_id", "name", "total_visits", "total_billed", "has_pending_payment"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for pid, summary in patient_summary.items():
        writer.writerow({
            "patient_id": pid,
            "name": summary["name"],
            "total_visits": summary["total_visits"],
            "total_billed": f"{summary['total_billed']:.2f}",
            "has_pending_payment": "Yes" if summary["has_pending_payment"] else "No"
        })

# Step 7: Write pending payments
with open(OUTPUT_FILE, "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=all_fields)
    writer.writeheader()
    writer.writerows(pending_rows)

# Step 8: Console summary
print("<======================== Console Summary ================================>")
print("Processed rows:", processed_rows)
print("Skipped rows:", skipped_rows)
print("Rows in pending_payments.csv:", len(pending_rows))
print("Rows in patient_summary.csv:", len(patient_summary))
