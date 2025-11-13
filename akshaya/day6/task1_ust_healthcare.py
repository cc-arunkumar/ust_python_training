# ust health care task
import csv
from collections import defaultdict

cleaned_data = []
skipped_rows = 0
# Read ust_healthcare_visits.csv with csv.DictReader .
with open('ust_healthcare_visits.csv',mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    
# Required fields: patient_id , name , visit_date , billed_amount , payment_status . If any
# missing → skip that row (and print a short message).
# Convert billed_amount to float (if conversion fails, skip row).
# Trim whitespace from string fields.
# Normalize payment_status to Title case (e.g., "pending" → "Pending" ).
# Normalize follow_up_required to "Yes" or "No" (treat empty as "No" ).

   
    for row in reader:
       
        if not row['patient_id'].strip() or not row['name'].strip() or not row['visit_date'].strip() or not row['billed_amount'].strip() or not row['payment_status'].strip():
            skipped_rows += 1
            print(f"Skipping row due to missing required field: {row}")
            continue

        
        row['name'] = row['name'].strip()
        row['visit_date'] = row['visit_date'].strip()
        row['payment_status'] = row['payment_status'].strip().title()
        row['follow_up_required'] = 'Yes' if row['follow_up_required'].strip().lower() in ['yes', 'y', '1'] else 'No'

        try:
            row['billed_amount'] = float(row['billed_amount'])
        except ValueError:
            skipped_rows += 1
            print(f"Skipping row due to invalid billed_amount: {row}")
            continue

        if row['payment_status'] not in ['Paid', 'Pending', 'Unpaid']:
            skipped_rows += 1
            print(f"Skipping row due to invalid payment_status: {row}")
            continue

        cleaned_data.append(row)
        
# Create outputs:
# pending_payments.csv : all cleaned columns for rows where payment_status != "Paid" .
# patient_summary.csv : aggregated per patient_id with columns:
# patient_id, name, total_visits, total_billed, has_pending_payment
# total_billed formatted with 2 decimals (e.g., 7500.00 ).
# has_pending_payment = "Yes" if any visit for that patient is not Paid;
# otherwise "No" .

with open('pending_payments.csv', 'w', newline='') as csvfile:
    fieldnames = ['patient_id', 'name', 'visit_date', 'department', 'billed_amount', 'insurance_provider', 'payment_status', 'contact', 'follow_up_required']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in cleaned_data:
        if row['payment_status'] != 'Paid':
            writer.writerow(row)

patient_summary = defaultdict(lambda: {'total_visits': 0, 'total_billed': 0.0, 'has_pending_payment': 'No'})

for row in cleaned_data:
    patient_summary[row['patient_id']]['total_visits'] += 1
    patient_summary[row['patient_id']]['total_billed'] += row['billed_amount']
    if row['payment_status'] != 'Paid':
        patient_summary[row['patient_id']]['has_pending_payment'] = 'Yes'

with open('patient_summary.csv', 'w', newline='') as csvfile:
    fieldnames = ['patient_id', 'name', 'total_visits', 'total_billed', 'has_pending_payment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for patient_id, data in patient_summary.items():
        row = {
            'patient_id': patient_id,
            'name': next((r['name'] for r in cleaned_data if r['patient_id'] == patient_id), ''),
            'total_visits': data['total_visits'],
            'total_billed': f"{data['total_billed']:.2f}",
            'has_pending_payment': data['has_pending_payment']
        }
        writer.writerow(row)

processed_rows = len(cleaned_data)
pending_rows = sum(1 for row in cleaned_data if row['payment_status'] != 'Paid')

print(f"Processed rows: {processed_rows}")
print(f"Skipped rows: {skipped_rows}")
print(f"Rows in pending_payments.csv: {pending_rows}")
print(f"Rows in patient_summary.csv: {len(patient_summary)}")


# sample output
# Skipping row due to missing required field: {'patient_id': 'P003', 'name': ' ', 'visit_date': '2025/10/02', 'department': 'Neurology', 'billed_amount': '3500.00', 'insurance_provider': '', 'payment_status': 'Unpaid', 'contact': '8800123456', 'follow_up_required': 'No'}
# Skipping row due to missing required field: {'patient_id': '', 'name': 'Meena Patel', 'visit_date': '2025-10-03', 'department': 'Cardiology', 'billed_amount': '2200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '7700123456', 'follow_up_required': 'No'}
# Skipping row due to invalid billed_amount: {'patient_id': 'P005', 'name': 'Suresh K', 'visit_date': '2025-10-03', 'department': 'General Medicine', 'billed_amount': 'one thousand', 'insurance_provider': 'HealthPlus', 'payment_status': 'Pending', 'contact': '9900112233', 'follow_up_required': 'Yes'}
# Skipping row due to invalid billed_amount: {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '2025-10-09', 'department': 'Cardiology', 'billed_amount': 'â‚¹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'No'}
# Skipping row due to missing required field: {'patient_id': 'P023', 'name': 'Sana Khan', 'visit_date': '', 'department': 
# 'Endocrinology', 'billed_amount': '3200.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Paid', 'contact': '7700022222', 'follow_up_required': 'No'}
# Skipping row due to invalid billed_amount: {'patient_id': 'P029', 'name': 'Liu Chen', 'visit_date': '2025-10-15', 'department': 'ENT', 'billed_amount': ' five thousand two hundred ', 'insurance_provider': 'MedSecure', 'payment_status': 'Pending', 'contact': '6000012222', 'follow_up_required': 'Yes'}
# Skipping row due to invalid billed_amount: {'patient_id': 'P040', 'name': 'Rachel Adams', 'visit_date': '2025-10-20', 'department': 'Endocrinology', 'billed_amount': '41OO.00', 'insurance_provider': 'EndoCare', 'payment_status': 'Pending', 
# 'contact': '7700035555', 'follow_up_required': 'No'}
# Skipping row due to invalid payment_status: {'patient_id': 'P052', 'name': 'Priya Menon', 'visit_date': '2025-10-24', 'department': 'ENT', 'billed_amount': 2.0, 'insurance_provider': '700.00', 'payment_status': 'Medsecure', 'contact': 'Pending', 'follow_up_required': 'No', None: ['No']}
# Skipping row due to invalid billed_amount: {'patient_id': 'P016', 'name': 'Sunil Sharma', 'visit_date': '2025-10-09', 'department': 'Cardiology', 'billed_amount': 'â‚¹8200.00', 'insurance_provider': 'MedSecure', 'payment_status': 'Paid', 'contact': '+91-98 100 12345', 'follow_up_required': 'No'}
# Processed rows: 101
# Skipped rows: 9
# Rows in pending_payments.csv: 56
# Rows in patient_summary.csv: 92
