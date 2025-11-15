# UST Healthcare CSV Read
import csv

# Initialization
processed = 0
skipped = 0
pending_rows = []
summary = {}

# Step 1: Read data from csv
with open('ust_healthcare_visit2.csv', 'r') as file:
    lines = file.readlines()

# Step 2: Extract header fields
header_line = lines[0].strip()
header = header_line.split(",")
index = {}
i = 0
while i < len(header):
    index[header[i]] = i
    i += 1

# Step 3: Process each row
for line in lines[1:]:
    row = line.strip().split(",")

    # Validate required fields
    if row[index['patient_id']] == '' or row[index['name']] == '' or row[index['visit_date']] == '' or row[index['billed_amount']] == '' or row[index['payment_status']] == '':
        print("Skipping row with missing required fields:", row)
        skipped += 1
        continue

    # Validate billed_amount
    billed_str = row[index['billed_amount']].strip()
    if not billed_str.replace('.', '', 1).isdigit():
        print("Skipping row with invalid billed_amount:", row)
        skipped += 1
        continue

    billed = round(float(billed_str), 2)
    payment_status = row[index['payment_status']].strip().title()
    follow_up = row[index['follow_up_required']].strip().lower()
    follow_up = 'Yes' if follow_up == 'yes' else 'No'

    # Clean and update row
    row[index['billed_amount']] = str(billed)
    row[index['payment_status']] = payment_status
    row[index['follow_up_required']] = follow_up
    processed += 1

    # Collect pending payments
    if payment_status != 'Paid':
        pending_rows.append(row)

    # Update patient summary
    pid = row[index['patient_id']]
    name = row[index['name']]
    gender = row[index['gender']] if 'gender' in index else ''
    if pid not in summary:
        summary[pid] = {
            'name': name,
            'gender': gender,
            'total_visits': 1,
            'total_billed': billed,
            'has_pending': payment_status != 'Paid'
        }
    else:
        summary[pid]['total_visits'] += 1
        summary[pid]['total_billed'] += billed
        if payment_status != 'Paid':
            summary[pid]['has_pending'] = True

# Step 4: Write pending_payments.csv
with open('pending_payments.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for row in pending_rows:
        writer.writerow(row)

# Step 5: Write patient_summary.csv
with open('patient_summary.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['patient_id', 'name', 'total_visits', 'total_billed', 'has_pending_payment', 'gender'])
    for pid, data in summary.items():
        writer.writerow([
            pid,
            data['name'],
            data['total_visits'],
            round(data['total_billed'], 2),
            'Yes' if data['has_pending'] else 'No',
            data['gender']
        ])

# Step 6: Console summary
print("Processed rows:", processed)
print("Skipped rows:", skipped)
print("Rows in pending_payments.csv:", len(pending_rows))
print("Rows in patient_summary.csv:", len(summary))

#sample Output

# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> & "C:/Program Files/Python314/python.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/task4_1_ust_healthcare_visit.py 
# Skipping row with missing required fields: ['', 'Meena Patel', '2025-10-03', 'Cardiology', '2200.00', 'MedSecure', 'Paid', '7700123456', 'No']
# Skipping row with invalid billed_amount: ['P005', 'Suresh K', '2025-10-03', 'General Medicine', 'one thousand', 
# 'HealthPlus', 'Pending', '9900112233', 'Yes']
# Skipping row with invalid billed_amount: ['P016', 'Sunil Sharma', '2025-10-09', 'Cardiology', 'â‚¹8200.00', 'MedSecure', 'Paid', '+91-98 100 12345', 'True']
# Skipping row with missing required fields: ['P023', 'Sana Khan', '', 'Endocrinology', '3200.00', 'EndoCare', 'Paid', '7700022222', 'No']
# Skipping row with invalid billed_amount: ['P029', 'Liu Chen', '2025-10-15', 'ENT', ' five thousand two hundred ', 'MedSecure', ' pending ', '6000012222', 'Yes']
# Skipping row with invalid billed_amount: ['P040', 'Rachel Adams', '2025-10-20', 'Endocrinology', '41OO.00', 'EndoCare', 'Pending', '7700035555', 'No']
# Skipping row with invalid billed_amount: ['P016', 'Sunil Sharma', '2025-10-09', 'Cardiology', 'â‚¹8200.00', 'MedSecure', 'Paid', '+91-98 100 12345', 'True']
# Processed rows: 103
# Skipped rows: 7
# Rows in pending_payments.csv: 58
# Rows in patient_summary.csv: 94