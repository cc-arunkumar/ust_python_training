# writing the data into the ust Health care csv file
import csv

# Data rows as a list of dictionaries
data = [
    {
        'patient_id': 'P001', 'name': 'Arun Kumar', 'visit_date': '2025-10-01',
        'department': 'Cardiology', 'billed_amount': '7500.00', 'insurance_provider': 'MedSecure',
        'payment_status': 'Paid', 'contact': '9810012345', 'follow_up_required': 'Yes'
    },
    {
        'patient_id': 'P002', 'name': 'Riya Sharma', 'visit_date': '2025-10-02',
        'department': 'Orthopedics', 'billed_amount': '12000.00', 'insurance_provider': 'HealthPlus',
        'payment_status': 'Pending', 'contact': '9810098765', 'follow_up_required': 'No'
    },
    {
        'patient_id': 'P003', 'name': 'John Doe', 'visit_date': '2025-10-02',
        'department': 'Neurology', 'billed_amount': '3500.00', 'insurance_provider': '',
        'payment_status': 'Unpaid', 'contact': '8800123456', 'follow_up_required': 'No'
    },
    {
        'patient_id': 'P004', 'name': 'Meena Patel', 'visit_date': '2025-10-03',
        'department': 'Cardiology', 'billed_amount': '2200.00', 'insurance_provider': 'MedSecure',
        'payment_status': 'Paid', 'contact': '7700123456', 'follow_up_required': 'No'
    },
    {
        'patient_id': 'P005', 'name': 'Suresh K', 'visit_date': '2025-10-03',
        'department': 'General Medicine', 'billed_amount': '1800.00', 'insurance_provider': 'HealthPlus',
        'payment_status': 'Pending', 'contact': '9900112233', 'follow_up_required': 'Yes'
    },
    {
        'patient_id': 'P006', 'name': 'Neha Verma', 'visit_date': '2025-10-04',
        'department': 'ENT', 'billed_amount': '4800.50', 'insurance_provider': 'MedSecure',
        'payment_status': 'Paid', 'contact': '9600001111', 'follow_up_required': 'No'
    },
    {
        'patient_id': 'P007', 'name': 'Alex Johnson', 'visit_date': '2025-10-04',
        'department': 'Neurology', 'billed_amount': '6000.00', 'insurance_provider': 'GlobalCare',
        'payment_status': 'Pending', 'contact': '7000005555', 'follow_up_required': 'Yes'
    }
]

# Write to CSV
with open('ust_healthcare_visits.csv', 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['patient_id', 'name', 'visit_date', 'department', 'billed_amount',
                  'insurance_provider', 'payment_status', 'contact', 'follow_up_required']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("CSV file 'ust_healthcare_visits.csv' created successfully.")
