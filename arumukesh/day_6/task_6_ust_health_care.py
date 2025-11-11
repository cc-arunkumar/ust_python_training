import csv

with open("ust_healthcare_visits.csv","r") as file:
    reader = csv.DictReader(file)
    with open("ust_health_care_visits_cleaned.csv","w", newline='') as file01:
        fieldnames = [f for f in reader.fieldnames if f and f.strip()]
        writer = csv.DictWriter(file01, fieldnames=fieldnames)
        writer.writeheader()
        processed_rows=0
        skipped_rows=0
        # declaring the mandatory fields for future reference
        required_fields = ['patient_id', "name", "visit_date", "billed_amount", "payment_status"]
        # to skip the values that don't fit in the fields or have none vals
        for rownumber,row in enumerate(reader,start=2):
            invalid_keys = [k for k in row.keys() if (k not in fieldnames or k is None)]
            if invalid_keys:
                print(f"Skipping row due to invalid keys: {invalid_keys} row number:{rownumber}")
                skipped_rows += 1
                continue
            # Check for missing required fields
            missing = [f for f in required_fields if not row.get(f, "").strip()]
            if missing:
                print("Fields missing:", missing)
                skipped_rows+=1
                continue

            # Clean billed amount
            billed_str = row.get("billed_amount", "").strip()
            try:
                row["billed_amount"] = float(billed_str) if billed_str else 0.0
            except ValueError:
                print(f" Invalid billed_amount for {row.get('patient_id')}: {billed_str}..skipping...")
                skipped_rows+=1
                continue

            # Strip string fields
            row = {k: v.strip() if isinstance(v, str) else v for k, v in row.items()}
            # Normalize payment_status
            row["payment_status"] = row["payment_status"].title()

            # Normalize follow_up_required
            follow_up = row.get("follow_up_required", "").strip().title()
            row["follow_up_required"] = "Yes" if follow_up == "Yes" else "No"
            processed_rows+=1
            writer.writerow(row)
        print(f"processed rows:{processed_rows}\n skipped rows:{skipped_rows}")

# Fields missing: ['name']
# Fields missing: ['patient_id']
#  Invalid billed_amount for P005: one thousand..skipping...
#  Invalid billed_amount for P016: â‚¹8200.00..skipping...
# Fields missing: ['visit_date']
#  Invalid billed_amount for P029: five thousand two hundred..skipping...
# Invalid billed_amount for P040: 41OO.00..skipping...
# Skipping row due to invalid keys: [None] row number:53
#Invalid billed_amount for P016: â‚¹8200.00..skipping...
# processed rows:101
#  skipped rows:9