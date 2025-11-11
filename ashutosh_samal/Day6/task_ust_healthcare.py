import csv
pending_payments = []
patient_summary = {}

# Open the CSV file
with open('ust_healthcare_visits.csv',"r",newline='') as csvfile:
    reader = csv.DictReader(csvfile)        
    # Iterate through each row
    for row in reader:
        # Basic field validation
        if row['patient_id'].strip()=="" or row['name'].strip()=="" or row['visit_date'].strip()=="" or row['billed_amount'].strip()=="" or row['insurance_provider'].strip()=="":
            print(f"Skipping row due to missing required field\n")
            continue
        try:
        # Convert billed_amount to float
            row['billed_amount'] = float(row['billed_amount'])
        except ValueError:
            print(f"Skipping row due to invalid billed_amount\n")
            continue
        
        # Trim whitespace from string fields
        row['patient_id'] = row['patient_id'].strip()
        row['name'] = row['name'].strip()
        row['visit_date'] = row['visit_date'].strip()
        row['payment_status'] = row['payment_status'].strip().title()
        row['follow_up_required'] = row['follow_up_required'].strip().capitalize()

        # Normalize payment_status and follow_up_required
        if row['follow_up_required'] == '':
            row['follow_up_required'] = 'No'
            row['payment_status'] = row['payment_status'].title()

        # Aggregating data for patient_summary
        patient_id = row['patient_id']
        if patient_id not in patient_summary:
            patient_summary[patient_id] = {
                'name': row['name'],
                'total_visits': 0,
                'total_billed': 0.0,
                'has_pending_payment': 'No'
            }

            patient_summary[patient_id]['total_visits'] += 1
            patient_summary[patient_id]['total_billed'] += row['billed_amount']

            if row['payment_status'] in ['Pending', 'Unpaid']:
                patient_summary[patient_id]['has_pending_payment'] = 'Yes'

        # If payment status is Pending or Unpaid, add to pending_payments list
        if row['payment_status'] in ['Pending', 'Unpaid']:
            pending_payments.append(row)
    
    with open('pending_payments.csv', mode='w', newline='') as pending_file:
        fieldnames = ['patient_id', 'name', 'dob', 'gender', 'contact', 'provider_id', 'provider_name', 'department', 'visit_date', 'visit_type', 'diagnosis_codes', 'procedure_codes', 'billed_amount', 'insurance_provider', 'insurance_id', 'payment_status', 'discharge_date', 'follow_up_required', 'notes']
        writer = csv.DictWriter(pending_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(pending_payments)

    # Write patient_summary.csv
    with open('patient_summary.csv', mode='w', newline='') as summary_file:
        fieldnames = ['patient_id', 'name', 'total_visits', 'total_billed', 'has_pending_payment']
        writer = csv.DictWriter(summary_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for patient_id, summary in patient_summary.items():
            summary['total_billed'] = f"{summary['total_billed']:.2f}"
            writer.writerow({
                'patient_id': patient_id,
                'name': summary['name'],
                'total_visits': summary['total_visits'],
                'total_billed': summary['total_billed'],
                'has_pending_payment': summary['has_pending_payment']
            })


#Sample Execution
# Skipping row due to missing required field

# Skipping row due to missing required field

# Skipping row due to invalid billed_amount 

# Skipping row due to missing required field

# Skipping row due to invalid billed_amount 

# Skipping row due to missing required field

# Skipping row due to missing required field

# Skipping row due to invalid billed_amount 

# Skipping row due to invalid billed_amount 