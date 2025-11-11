# UST Healthcare (CSV Read / Write)
# Duration: 20–30 minutes
# Goal: Read a CSV of clinic visits, perform cleaning/validation, then write two
# reports:
# 1. pending_payments.csv — visits not marked Paid.
# 2. patient_summary.csv — one row per patient with total_visits and total_billed .
# 3. Create outputs:
# pending_payments.csv : all cleaned columns for rows where payment_status != "Paid" .
# patient_summary.csv : aggregated per patient_id with columns:
# patient_id, name, total_visits, total_billed, has_pending_payment
# total_billed formatted with 2 decimals (e.g., 7500.00 ).
# has_pending_payment = "Yes" if any visit for that patient is not Paid;
# otherwise "No" .
# 4. Console summary: print counts: processed rows, skipped rows, rows in each
# output.

import csv

summary_dictionary = {}
iteration_count = 0

# These are the fields we must have for each row
required_fields = ["patient_id", "name", "visit_date", "billed_amount", "payment_status"]

# Open the healthcare file
with open('ust_healthcare_visits.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Read the first line (header)
    header = next(csv_reader)

    # Create a dictionary that stores each column name and its position
    column_index = {}
    for i in range(len(header)):
        column_index[header[i]] = i

    # Check if all required fields are present in the file
    for field in required_fields:
        if field not in column_index:
            print(f"Missing required column in file: {field}")
            exit()

    # Go through each row in the CSV
    for row in csv_reader:
        if len(row) < len(required_fields):
            continue

        # Get data from the correct column (using the header positions)
        patient_id = row[column_index["patient_id"]].strip()
        patient_name = row[column_index["name"]].strip()
        visit_date = row[column_index["visit_date"]].strip()
        billed_amount_text = row[column_index["billed_amount"]].strip()
        payment_status = row[column_index["payment_status"]].strip().capitalize()

        # Skip the row if any required field is blank
        if (patient_id == "" or patient_name == "" or visit_date == "" 
            or billed_amount_text == "" or payment_status == ""):
            print("Row skipped — for mising error")
            continue

        # Try to convert billed amount to a number
        try:
            billed_amount = float(billed_amount_text)
        except ValueError:
            print("Row skipped — for float error")
            continue

        # Add the data to our summary dictionary
        if patient_id not in summary_dictionary:
            summary_dictionary[patient_id] = {
                "name": patient_name,
                "total_visits": 0,
                "total_bill": 0.0,
                "status": payment_status
            }

        # Update total visits and total bill
        summary_dictionary[patient_id]["total_visits"] += 1
        summary_dictionary[patient_id]["total_bill"] += billed_amount

# Write the output to a new CSV file
with open('patient_summary.csv', 'w', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(required_fields)

    for pid, data in summary_dictionary.items():
        writer.writerow([
            pid,
            data["name"],
            data["total_visits"],
            data["total_bill"],
            data["status"]
        ])
print("Process completed successfully!")

# sample output:
# Row skipped — for mising error
# Row skipped — for mising error
# Row skipped — for float error
# Row skipped — for float error
# Row skipped — for mising error
# Row skipped — for float error
# Row skipped — for float error
# Row skipped — for float error
# Process completed successfully!
