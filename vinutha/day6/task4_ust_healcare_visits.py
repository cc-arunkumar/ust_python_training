# UST Healthcare (CSV Read / Write)
import csv

# initialization
processed = 0
skipped = 0
pending_rows = []
summary = {}

# Step 1: Reading data from csv
with open('ust_healthcare_visits1.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Step 2: Validate required fields
        if row['patient_id'] == '' or row['name'] == '' or row['visit_date'] == '' or row['billed_amount'] == '' or row['payment_status'] == '':
            print("Skipping row with missing required fields:", row)
            skipped += 1
            continue

        # Step 2: Convert billed_amount to float
        if row['billed_amount']:
            billed = float(row['billed_amount'])
        else:
            print("Skipping row with invalid billed_amount:", row)
            skipped += 1
            continue

        # Step 2: Remove leading and trailing spaces
        for key in row:
            row[key] = row[key].strip()

        # Step 2: Normalize fields
        row['payment_status'] = row['payment_status'].title()
        if row['follow_up_required'].lower() == 'yes':
            row['follow_up_required'] = 'Yes'
        else:
            row['follow_up_required'] = 'No'

        row['billed_amount'] = round(billed, 2)
        processed += 1
    
        # Step 3: Collects pending payments
        if row['payment_status'] != 'Paid':
            pending_rows.append(row)

        # Step 3: Update patient summary
        pid = row['patient_id']
        if pid not in summary:
            summary[pid] = {
                'name': row['name'],
                'total_visits': 1,
                'total_billed': billed,
                'has_pending': row['payment_status'] != 'Paid'
            }
        else:
            summary[pid]['total_visits'] += 1
            summary[pid]['total_billed'] += billed
            if row['payment_status'] != 'Paid':
                summary[pid]['has_pending'] = True

# Step 3: Write data into pending_payments.csv
with open('pending_payments.csv', 'w', newline='') as file:
    # fields=file.split(",")
    fields = ['patient_id', 'name', 'dob', 'gender', 'contact', 'provider_id', 'provider_name',
          'department', 'visit_date', 'visit_type', 'diagnosis_codes', 'procedure_codes',
          'billed_amount', 'insurance_provider', 'insurance_id', 'payment_status',
          'discharge_date', 'follow_up_required', 'notes']

    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for row in pending_rows:
        writer.writerow(row)

# Step 3: Writing data into patient_summary.csv
with open('patient_summary.csv', 'w', newline='') as file:
    fields = ['patient_id', 'name', 'total_visits', 'total_billed', 'has_pending_payment', 'gender']
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for pid in summary:
        writer.writerow({
            'patient_id': pid,
            'name': summary[pid]['name'],
            'total_visits': summary[pid]['total_visits'],
            'total_billed': round(summary[pid]['total_billed'], 2),
            'has_pending_payment': 'Yes' if summary[pid]['has_pending'] else 'No'
        })

# Step 4: Console summary
print("Processed rows:", processed)
print("Skipped rows:", skipped)
print("Rows in pending_payments.csv:", len(pending_rows))
print("Rows in patient_summary.csv:", len(summary))


# #sample Output for sample data
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/task4_ust_healcare_visits.py
# Processed rows: 7
# Skipped rows: 0
# Rows in pending_payments.csv: 4
# Rows in patient_summary.csv: 7
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> 


#sample Output for new csv file
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/task4_ust_healcare_visits.py
# Processed rows: 100
# Skipped rows: 0
# Rows in pending_payments.csv: 54
# Rows in patient_summary.csv: 100
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6>